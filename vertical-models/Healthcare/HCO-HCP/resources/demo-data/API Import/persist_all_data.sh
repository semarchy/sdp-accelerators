#!/bin/bash

# Curl script to persist ALL data with PERSIST_DATA action
# Auto-generated from all CSV files in the API Import directory

# Configuration
API_KEY="YOUR_API_KEY"
BASE_URL="https://<sdp-tenant-name>/dm/api/rest"
MODEL_NAME="JPE_HCO_HCP"
# Set to a valid job name from the server list (e.g. DDJ_Products), or leave empty to skip submit.
SUBMIT_JOB="ALL_DATA"

# Create load and retrieve loadId
echo "=== Creating HCO-HCP load ==="
CREATE_LOAD_RESPONSE=$(curl --silent --location --globoff "$BASE_URL/loads/$MODEL_NAME" \
    --header "Content-Type: application/json" \
    --header "API-Key: $API_KEY" \
    --data '{
        "action": "CREATE_LOAD",
        "programName": "bulk",
        "loadDescription": "Load ALL HCO-HCP Demo Data"
    }')
LOAD_ID=$(echo "$CREATE_LOAD_RESPONSE" | grep -o '"loadId"[ ]*:[ ]*[0-9]*' | grep -o '[0-9]*')

if [ -z "$LOAD_ID" ]; then
    echo "Error: Unable to retrieve loadId. Response: $CREATE_LOAD_RESPONSE"
    exit 1
fi

echo "Load created with loadId = $LOAD_ID"

# Endpoint for PERSIST_DATA action
ENDPOINT="$BASE_URL/loads/$MODEL_NAME/$LOAD_ID"

echo "=== Persisting all data ==="
echo "Endpoint: $ENDPOINT"
echo "Load ID: $LOAD_ID"
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CSV_DIR="$SCRIPT_DIR/../UI Import"

PYTHON_BIN=""
if command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
else
  echo "ERROR: python or python3 is required on PATH." >&2
  exit 1
fi

# Function to make a curl call for an entity
persist_entity() {
    local entity_name="$1"
    local csv_file="$2"

    if [ ! -f "$csv_file" ]; then
        echo "WARN: Missing CSV for $entity_name: $csv_file"
        echo ""
        return 0
    fi

    local entity_data
    entity_data=$($PYTHON_BIN - "$entity_name" "$csv_file" <<'PY'
import csv
import json
import sys

entity = sys.argv[1]
csv_file = sys.argv[2]

def normalize_header(name: str) -> str:
    return name.lstrip("\ufeff")

def truthy(value: str) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}

def get(row, key):
    return (row.get(key) or "").strip()

NUMERIC_FIDS = {
    "FID_Sponsor",
    "FID_Form",
    "FID_Administration",
}

def normalize_fid(value: str, target: str):
    # Only cast to int for known numeric foreign IDs; keep others as strings.
    cleaned = value.replace(",", "").strip()
    if target in NUMERIC_FIDS and cleaned.isdigit():
        return int(cleaned)
    return cleaned

def map_row(row, mapping):
    record = {}
    for target, source in mapping.items():
        val = get(row, source)
        if val != "":
            if target.startswith("FID_"):
                val = normalize_fid(val, target)
            record[target] = val
    return record

def map_member_ids(row):
    mapping = [
        ("MemberIDs.UMI", "Member IDs (UMI)", "UMI"),
        ("MemberIDs.enGenAgreementNumber", "Member IDs (en Gen Agreement Number)", "en Gen Agreement Number"),
        ("MemberIDs.enGenConsumerID", "Member IDs (en Gen Consumer ID)", "en Gen Consumer ID"),
        ("MemberIDs.PlanPartnerID", "Member IDs (Plan Partner ID)", "Plan Partner ID"),
        ("MemberIDs.ClientAssignedMemberID", "Member IDs (Client Assigned Member ID)", "Client Assigned Member ID"),
        ("MemberIDs.PMI", "Member IDs (PMI)", "PMI"),
        ("MemberIDs.MNPPID", "Member IDs (MNPP ID)", "MNPP ID"),
        ("MemberIDs.MNPPMemberCK", "Member IDs (MNPP Member CK)", "MNPP Member CK"),
        ("MemberIDs.MAXIS", "Member IDs (MAXIS)", "MAXIS"),
        ("MemberIDs.Auth0ID", "Member IDs (Auth0 ID)", "Auth0 ID"),
        ("MemberIDs.ClearstoneID", "Member IDs (Clearstone ID)", "Clearstone ID"),
        ("MemberIDs.BCBSALID", "Member IDs (BCBSAL ID)", "BCBSAL ID"),
        ("MemberIDs.DHSID", "Member IDs (DHS ID)", "DHS ID"),
    ]
    out = {}
    for target, primary, fallback in mapping:
        val = get(row, primary) or get(row, fallback)
        if val:
            out[target] = val
    return out

with open(csv_file, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames or []
    reader.fieldnames = [normalize_header(n) for n in fieldnames]
    rows = list(reader)

records = []

if entity == "Administration":
    mapping = {"RouteOfAdministration": "Route Of Administration"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Form":
    mapping = {"Form": "Form"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "HCO":
    mapping = {
        "PublisherID": "Publisher ID",
        "SourceID": "Source ID",
        "HospitalName": "Hospital Name",
        "HospitalNameNormalized": "Hospital Name Normalized",
        "HospitalCCN": "Hospital CCN",
        "HospitalID": "Hospital ID",
        "inpstreet": "Street",
        "inpcity": "City",
        "inpstate": "State",
        "inpzip": "Zip",
        "inpcountry": "Country",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "HCP":
    mapping = {
        "PublisherID": "Publisher ID",
        "SourceID": "Source ID",
        "PublisherID_HCO": "HCO   (Publisher ID)",
        "SourceID_HCO": "HCO   (Source ID)",
        "PhysicianProfileID": "Physician Profile ID",
        "FirstName": "First Name",
        "MiddleName": "Middle Name",
        "LastName": "Last Name",
        "NameSuffix": "Name Suffix",
        "StreetAddressLine1": "Street Address Line1",
        "StreetAddressLine2": "Street Address Line2",
        "City": "City",
        "State": "State",
        "ZipCode": "Zip Code",
        "Country": "Country",
        "Province": "Province",
        "PostalCode": "Postal Code",
        "PrimaryType": "Primary Type",
        "Specialties": "Specialties",
        "LicenseStateCode1": "License State Code 1",
        "LicenseNumber1": "License Number 1",
        "LicenseStateCode2": "License State Code 2",
        "LicenseNumber2": "License Number 2",
        "LicenseStateCode3": "License State Code 3",
        "LicenseNumber3": "License Number 3",
        "LicenseStateCode4": "License State Code 4",
        "LicenseNumber4": "License Number 4",
        "LicenseStateCode5": "License State Code 5",
        "LicenseNumber5": "License Number 5",
        "FID_TaxonomySpecialization": "Taxonomy Specialization   (Foreign ID)",
        "NPI": "NPI",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "HCPSpecialty":
    mapping = {
        "ID": "ID",
        "FID_Specialty": "Specialty   (Foreign ID)",
        "PublisherID_HCP": "HCP   (Publisher ID)",
        "SourceID_HCP": "HCP   (Source ID)",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "ICD10CM":
    mapping = {
        "ID": "id",
        "OrderNumber": "order_number",
        "ShortDescription": "short_description",
        "LongDescription": "long_description",
        "FormattedICD10Code": "formatted_icd10_code",
        "FID_ParentICD10": "FDN_parenticd10",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "ICD9CM":
    mapping = {
        "ID": "id",
        "Description": "description",
        "RawICD9Code": "raw_icd9_code",
        "FID_ParentICD9": "fdn_parenticd9",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if "is_industry_std" in row and row["is_industry_std"] != "":
            rec["IsIndustryStd"] = truthy(row["is_industry_std"])
        if rec:
            records.append(rec)

elif entity == "ICDMapping":
    mapping = {
        "ICDMappingID": "icd_mapping_id",
        "Description": "description",
        "FID_ICD10": "fdn_icd10",
        "FID_ICD9": "fdn_icd9",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "InsuranceCompany":
    mapping = {
        "Code": "Code",
        "Name": "Name",
        "TypeOfPayments": "TypeOfPayments",
        "URL": "URL",
        "InputAddress.Street": "Street",
        "InputAddress.City": "City",
        "InputAddress.State": "State",
        "InputAddress.Zip": "Zip",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Member":
    mapping = {
        "PublisherID": "Publisher ID",
        "SourceID": "Source ID",
        "PublisherID_HCP": "HCP   (Publisher ID)",
        "SourceID_HCP": "HCP   (Source ID)",
        "SINumber": "SI Number",
        "FirstName": "First Name",
        "MiddleName": "Middle Name",
        "LastName": "Last Name",
        "Suffix": "Suffix",
        "Gender": "Gender",
        "BirthDate": "Birth Date",
        "DeathDate": "Death Date",
        "MemberIDX": "Member IDX",
        "GroupID": "Group ID",
        "HomePhone": "Home Phone",
        "MaritalStatus": "Marital Status",
        "GroupName": "Group Name",
        "SubscriberRelationship": "Subscriber Relationship",
        "PlaceOfBirth": "Place Of Birth",
        "WorkPhone": "Work Phone",
        "CellPhone": "Cell Phone",
        "EmailAddress": "Email Address",
        "PrimaryPhysicianID": "Primary Physician ID",
        "Street": "Street",
        "City": "City",
        "State": "State",
        "Zip": "Zip",
        "Country": "Country",
    }
    for row in rows:
        rec = map_row(row, mapping)
        rec.update(map_member_ids(row))
        if rec:
            records.append(rec)

elif entity == "Coverage":
    mapping = {
        "SubscriberID": "Subscriber ID",
        "GroupName": "Group Name",
        "EffectiveDate": "Effective Date",
        "GroupNumber": "Group Number",
        "ExpirationDate": "Expiration Date",
        "Relationship": "Relationship",
        "FID_InsuranceCompany": "Insurance Company   (Foreign ID)",
        "PublisherID_Member": "Member   (Publisher ID)",
        "SourceID_Member": "Member   (Source ID)",
        "PublisherID_Subscriber": "Subscriber   (Publisher ID)",
        "SourceID_Subscriber": "Subscriber   (Source ID)",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Encounter":
    mapping = {
        "EncounterID": "Encounter ID",
        "EncounterDate": "Encounter Date",
        "Condition": "Condition",
        "Medication": "Medication",
        "PublisherID_HCO": "HCO   (Publisher ID)",
        "SourceID_HCO": "HCO   (Source ID)",
        "PublisherID_HCP": "HCP   (Publisher ID)",
        "SourceID_HCP": "HCP   (Source ID)",
        "PublisherID_Member": "Member   (Publisher ID)",
        "SourceID_Member": "Member   (Source ID)",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Products":
    mapping = {
        "PublisherID": "Publisher ID",
        "SourceID": "Source ID",
        "TradeName": "Trade Name",
        "ProductName": "Product Name",
        "GenericName": "Generic Name",
        "NDCCode": "NDC Code",
        "Indication": "Indication",
        "Price": "Price",
        "Definition": "Definition",
        "url": "url",
        "FID_TherapeauticArea": "Therapeautic Area   (Foreign ID)",
        "FID_Sponsor": "Sponsor   (Foreign ID)",
        "FID_Form": "Form   (Foreign ID)",
        "FID_Administration": "Administration   (Foreign ID)",
        "GEN_AIDescription": "GEN AI Description",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Specialty":
    mapping = {"Code": "Code", "Name": "Name"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Sponsor":
    mapping = {"SponsorName": "Sponsor Name"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "Strength":
    mapping = {
        "Strength": "Strength",
        "PublisherID_Products": "Products (Publisher ID)",
        "SourceID_Products": "Products (Source ID)",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "TaxonomyGrouping":
    mapping = {"ID": "ID", "Name": "Name", "Role": "Role"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "TaxonomyClassification":
    mapping = {
        "ID": "ID",
        "FID_Grouping": "Grouping   (Foreign ID)",
        "ClassificationCode": "Classification Code",
        "Name": "Name",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "TaxonomySpecialization":
    mapping = {"ID": "ID", "Name": "Name"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "TaxonomyClassificationSpecialization":
    mapping = {
        "ID": "Code",
        "FID_Classification": "Classification   (Foreign ID)",
        "FID_TaxonomySpecialization": "Taxonomy Specialization   (Foreign ID)",
        "Definition": "Definition",
        "Notes": "Notes",
    }
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

elif entity == "TherapeauticArea":
    mapping = {"Code": "Code", "Name": "Name", "Description": "Description"}
    for row in rows:
        rec = map_row(row, mapping)
        if rec:
            records.append(rec)

else:
    raise SystemExit(f"Unknown entity: {entity}")

print(json.dumps(records, ensure_ascii=True))
PY
)

    echo "=== Persisting entity: $entity_name ==="

    local payload_file
    payload_file="$(mktemp)"
    cat > "$payload_file" <<JSON
{
  "action": "PERSIST_DATA",
  "persistOptions": {
    "responsePayload": "SUMMARY",
    "persistMode": "IF_NO_ERROR_OR_MATCH",
    "missingIdBehavior": "GENERATE",
    "optionsPerEntity": {}
  },
  "persistRecords": {
    "$entity_name": $entity_data
  }
}
JSON

    curl -X POST \
        "$ENDPOINT" \
        -H "Content-Type: application/json" \
        -H "Api-Key: $API_KEY" \
        --data-binary "@$payload_file"

    rm -f "$payload_file"

    echo ""
    echo "--- End of $entity_name ---"
    echo ""
}

# 1. Administration
echo "1/22 - Persisting Administration..."
persist_entity "Administration" "$CSV_DIR/02-Administration.csv"

# 2. Form
echo "2/22 - Persisting Form..."
persist_entity "Form" "$CSV_DIR/03-Forms.csv"

# 3. Sponsor
echo "3/22 - Persisting Sponsor..."
persist_entity "Sponsor" "$CSV_DIR/10-Sponsors.csv"

# 4. TherapeauticArea
echo "4/22 - Persisting TherapeauticArea..."
persist_entity "TherapeauticArea" "$CSV_DIR/20-Therapeautic Areas.csv"

# 5. Products
echo "5/22 - Persisting Products..."
persist_entity "Products" "$CSV_DIR/21-Products.csv"

# 6. Strength
echo "6/22 - Persisting Strength..."
persist_entity "Strength" "$CSV_DIR/22-Strengths.csv"

# 7. InsuranceCompany
echo "7/22 - Persisting InsuranceCompany..."
persist_entity "InsuranceCompany" "$CSV_DIR/08-Insurance Companies.csv"

# 8. HCO
echo "8/22 - Persisting HCO..."
persist_entity "HCO" "$CSV_DIR/04-HCOs.csv"

# 9. HCP
echo "9/22 - Persisting HCP..."
persist_entity "HCP" "$CSV_DIR/15-HCPs.csv"

# 10. Specialty
echo "10/22 - Persisting Specialty..."
persist_entity "Specialty" "$CSV_DIR/09-Specialties.csv"

# 11. HCPSpecialty
echo "11/22 - Persisting HCPSpecialty..."
persist_entity "HCPSpecialty" "$CSV_DIR/16-HCP Specialties.csv"

# 12. TaxonomyGrouping
echo "12/22 - Persisting TaxonomyGrouping..."
persist_entity "TaxonomyGrouping" "$CSV_DIR/11-Taxonomy Groupings.csv"

# 13. TaxonomyClassification
echo "13/22 - Persisting TaxonomyClassification..."
persist_entity "TaxonomyClassification" "$CSV_DIR/12-Taxonomy Classifications.csv"

# 14. TaxonomySpecialization
echo "14/22 - Persisting TaxonomySpecialization..."
persist_entity "TaxonomySpecialization" "$CSV_DIR/13-Taxonomy Specializations.csv"

# 15. TaxonomyClassificationSpecialization
echo "15/22 - Persisting TaxonomyClassificationSpecialization..."
persist_entity "TaxonomyClassificationSpecialization" "$CSV_DIR/14-Taxonomy Classification Specializations.csv"

# 16. ICD9CM
echo "16/22 - Persisting ICD9CM..."
persist_entity "ICD9CM" "$CSV_DIR/06-ICD9.csv"

# 17. ICD10CM
echo "17/22 - Persisting ICD10CM..."
persist_entity "ICD10CM" "$CSV_DIR/05-ICD-10-CM.csv"

# 18. ICDMapping
echo "18/22 - Persisting ICDMapping..."
persist_entity "ICDMapping" "$CSV_DIR/07-ICDMappings.csv"

# 19. Member
echo "19/22 - Persisting Member..."
persist_entity "Member" "$CSV_DIR/17-Members.csv"

# 20. Coverage
echo "20/22 - Persisting Coverage..."
persist_entity "Coverage" "$CSV_DIR/18-Coverages.csv"

# 21. Encounter
echo "21/22 - Persisting Encounter..."
persist_entity "Encounter" "$CSV_DIR/19-Encounters.csv"

echo "=== COMPLETE PERSISTENCE FINISHED ==="
echo "All 22 entities have been processed."

# Remote load submission/validation (to be done last)
if [ -n "$SUBMIT_JOB" ]; then
  echo "=== Remote load validation (SUBMIT) ==="
  SUBMIT_RESPONSE=$(curl --silent --location --globoff "$BASE_URL/loads/$MODEL_NAME/$LOAD_ID" \
      --header "Content-Type: application/json" \
      --header "API-Key: $API_KEY" \
      --data "{
          \"action\": \"SUBMIT\",
          \"jobName\": \"$SUBMIT_JOB\",
          \"submitAs\": \"Demo.Initiator\"
      }")
  echo "Validation response: $SUBMIT_RESPONSE"
else
  echo "=== SUBMIT skipped (SUBMIT_JOB is empty) ==="
fi
