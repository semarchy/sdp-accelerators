(c) Semarchy 2026

This file explains how to import the dashboard into the Corporate Finance application.

Instructions:
    1- rename the archive file "CorpFinDashboard.rename_to_zip" to CorpFinDashboard.zip
    2- On the SDP homepage go to Tools -> Dashboard Builder
    3- Select Import Application
    4- Drag & Drop CorpFinDashboard.zip
    5- Once imported go to Queries -> MissingCounterpartyAttributes -> Open Query Properties -> Query actions -> OpenRecord
    6- Adjust the URL to reflect the correct dataloc: 
        mdm-app/<SET_CORRECT_DATALOC_HERE>/CorpFinApplication/browsing/CounterpartyBusinessView/${Counterparty ID}

        Example: mdm-app/sdpal_corpfin/CorpFinApplication/browsing/CounterpartyBusinessView/${Counterparty ID}
    7- Save