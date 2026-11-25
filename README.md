## Project overview

The SDP Accelerators Library is a project designed to host reusable data models and individual components for Semarchy Data Platform (SDP). 
This library aims to help customers and partners quickly start new SDP projects and build upon a Semarchy certified foundation. 
This library includes MVP-ready industry models with documentation and guidelines, as well as reusable components like a "4 eyes principle" workflow.

It is maintained and released by Semarchy Professional Services team. 

## Documentation

Each use-case specific model includes user guide covering:
- the use case overview
- data model detailed structure
- design decisions on matching, workflows, validation and enrichers
- guidance on possible extensions and customizations for this data model
- recommendations on how to use this model in conjunction with Semarchy Rapid Delivery Blueprint

Each reusable component includes in-file documentation and description tags as well as a header comment with useful information.


## How to use?

You can simply check out the model or download the component that you want to use in your project from our GitHub repository.
You will need to adjust package name for the components to fit into your model structure. 


### Prerequisites

To work on an accelerator for SDP AL, you need the following prerequisites:
- Install Visual Studio Code and activate GitHub extension
- Semarchy VS Code Extension
- Semarchy CLI (Design and Platform)

To deploy your accelerator, you will also need a Semarchy Data Platform instance, in SaaS or in a Self-Hosted environment. If you don't have already an instance, please [contact us](https://semarchy.com/free-trial/).

### Getting started

1. Clone repository

1.1. Cloning repository through VS Code extension:

- In the VS Code go to Source Control tab
- Display repositories
- Click on the three dots to get context menu and choose Clone
- Clone from GitHub
- Select sdp-accelerators repository to clone

1.2. Cloning through command line

You can do same using a git command line:

```git clone https://github.com/semarchy/sdp-accelerators.git ```


2. Creating your workspace

If you are working on a new use-case model you need to create a new workspace:

- inside the sdp-accelerators project under use-case-models create a new folder named as your model in camel case
- go to VS Code and open a workspace selecting this folder as root folder.

If you want to use an existing use-case model for demo purposes, we recommend creating a workspace that will use the existing model folder as root. 

If you want to use an existing use-case model and customize it for your own project, we recommend creating a separate workspace not connected to Semarchy GitHub and copy files in there. You can then connect it to your own version control system and set up CI/CD chain.

3. Set up Semarchy Extension

Follow Semarchy official documentation to set up your extension with instance connection information and API Key.
You can use the setting.json.template in an existing model folder to check what the model root parameter looks like.

### Build & Deploy existing model

Go to Semarchy Extension panel and use Build & Deploy button to build your workspace and deploy it on your target instance.

Once build and deploy are successful you can access the Data product on your SDP Home page.

You can now import test data from the test datasets and start exploring the existing model 

### Start development

- Make sure to follow your company DevOpps guidelines:
- access your company version control system
- connect your local project with Semarchy template files to a repository there
- follow DevOpps guidelines in terms of git flow and collaboration
- test your changes on your development server.

## Code and collaboration guidelines

- Each file in the code base must have leading comments regarding the general purpose of the file

- Each object in the model that can have description and documentation attribute must have meaningful description and documentation. 

- Folder structure inside a use-case specific model must follow Semarchy official guidelines

- Naming convention: Semarchy naming convention must be applied for all files (camel case)

```<Object name>.<Object type>.seml ```

- Make sure to pull often or configure auto-pull

- Don’t forget to commit/push before the end of the day

- Conflict resolution must be done properly through Git tool by reviewer when merging pull request. If you get conflicts during pull - resolve them with care on your local branch.

- Make sure that your model compiles (Semarchy build is OK) before pushing it and submitting for review.

## Use-case model structure

Each use-case model accelerator included in the library must follow the predefined structure.

Each folder has its own goal and structure:

- .vscode - it is an optional folder that should only have one file, called settings.json.template and define the semarchy.dm.modelFolderPath for the model. Whenever starting to work with the accelerator, the user will check out the code base and use this template file to create their own settings.

- documentation - it is a mandatory folder that must contain markdown formatted end-user and developer documentation for the model. See Documentation structure for more details on the content.

- resources - any images or files that are used in the model or in the documentation. For example, it is a good place to put the image library associated with the model.

- src - this folder hosts the actual source code for the data model according to Semarchy best practices.

- README.md - main README file of the use-case model that can contain just a brief summary with the link to the user guide page from the documentation. Any other high-level info can be included (version, author, specific considerations etc.)

Each data model must be submitted with a test data set. This data sets must be in a format that is easily importable in SDP (CSV, Excel) and contain some representative data for the use case. File size for each dataset is limited to 1MB. 

The goal of test data set is to help get a feeling of what data the model is covering, illustrate matching rules, help the customer to quickly set up a business demo on their side. It can also be used to set up unit/functional testing for the model. 

The dataset must not contain any real data of personal or confidential type. You can use a generator (1, 2) to create this dataset.

## Use-case model documentation structure

The documentation is a very important part of the SDP Accelerators library as the aim of the project is to provide a self-service accelerators for Semarchy customers and partners.

Each use-case model documentation must include the following chapters:

### Introduction & use case description

In this chapter the goal is to describe the use case for this model and what business domain it covers. It can also explain main capabilities and business value of the accelerator as well as audience for such MDM implementation.

### Model structure

This chapter must include a model diagram (Semarchy → Open in diagram view) and detailed description of the structure of entities and their attributes. 

We recommend creating a separate model_structure.md file with tables presenting detailed information.

For example, to describe entities you can create a table having the following columns: 

| Entity Name | Entity Label | Entity Documentation | Referenced by Entities | References Entities | Number of Attributes |

And for each entity create a detailed tables presenting attributes:

| Attribute name | Attribute label | Data type | Mandatory? | Description | Used in matching |

You can create both tables by using GitHub Copilot with the following prompts:

```Create file model_structure.md in the documentation folder and add in there a markdown table with the following columns: Entity Name, Entity Label, Entity Documentation, Referenced by Entities, References Entities, Number of Attributes. To populate this table use the information available in files situated in entities folder and its subfolders with the name ending with Entity.seml. To populate references information, use files in the references folder. ```

``` Update the file model_structure.md in the documentation folder to add a markdown table for each entity in the model. The table must have the following columns: Attribute name, Attribute label, Data type, Mandatory?, Description, Used in matching. The information about attributes is available in files in entities folder and its subfolder with the name ending with Entity.seml. Attribute is used in matching if it is referenced in the matcher property and/or its children in the entity definition. ```

N.B. If you have a lot of entities in the model, you might want to run these requests in batches to avoid Copilot failing.

### Main entities description

For each of the main entities this chapter must provide information about matching rules if applicable, specific enrichers or validation and design of the hierarchies (if applicable).

### Model components description

This chapter must cover main components such as enrichers, validations, duplicate managers, survivorship rules, workflows that are relevant for the customer to understand how to use the model. 

### Work for developers 

This chapter must describe, how the customer can use the model at the early stages of the project and what development work can be done to extend and customize the model for their company. 

### General tips:

- use simple English

- if you generate description with an AI tool, humanize it for better understanding

- include tips and links to Semarchy documentation whenever possible.

## Reusable component structure

Reusable components can be composed of one or several seml files depending on what you are implementing. 

Each file must have an meaningful comment in the beginning to describe the usage of the component and any particular considerations. 

Component files must be placed in relevant subfolders of the reusable-components folder according to their type.
