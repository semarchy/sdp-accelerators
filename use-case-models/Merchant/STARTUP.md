# Design structure overview

A typical Semarchy design workspace should be organized as follows:
- the `src` package contains all the source code of your design-time objects
- the `resources` package contains the non-code files, like images and payloads used by the REST API


# Get started overview

To start the design of your data product, you'll need to:
1- Create an API-key using the Semarchy Platform CLI
2- Create your data model under the `src` package
3- Configure the Semarchy Data Platform extension


More details are available here: https://docs.semarchy.com/sdp/platform/start


# 1- Create an API-key using the Semarchy Platform CLI

## Prepare access credentials
To complete the configuration of the Semarchy Data Platform extension and enable all its features, you must provide a valid access credential in the form of an API key.
API keys are generated using the Semarchy Platform CLI available here: https://docs.semarchy.com/sdp/platform/admin/install-platform-cli

1. Download the Semarchy Platform CLI archive.
2. Extract the contents of the ZIP archive to your preferred location.
3. Inside the extracted folder, identify the compressed file that matches your operating system and extract its contents.
4. Open a terminal or command prompt and verify the installation:
    ```
    sem version
    ```
    The output should show the version number of the Platform CLI.

## Authenticate with the Platform CLI
To operate the platform, the Platform CLI must use an authenticated session. The session duration is two hours by default and resets each time the CLI is used.

1. Run the following command, replacing `<url>` with the endpoint for your Data Platform instance:
   ```
   sem auth login <url>
   ```
   The CLI prompts you to log in through a browser.
2. In the browser, follow the instructions to sign in and authorize CLI access to the platform API.
3. Confirm that authentication is successful by running a module-specific command, such as the following for Data Management:
   ```
   sem dm admin status
   ```
   If authenticated, the command returns the module's status without errors.

## Create an API-Key
1. Verify and update the content of `semDmApiKey_config.json`.
2. Navigate to the data product package.
3. Run the following command:
   ```
   sem dm admin api-key create -i /resources/semDmApiKey_config.json
   ```


# 2- Create your data model under the `src` package

Right click on the `src` package and select Semarchy > **Semarchy: Create Model**.


# 3- Configure the Semarchy Data Platform extension

Configure the extension to connect to an existing Data Management instance.

1. In the Extension view, locate the Semarchy Data Platform extension and click the **Settings** icon.
2. In the contextual menu, select **Settings**.
3. Select the **Workspace** tab.
4. Set the following properties:
    - **API Key**: the API key created in the previous step.
    - **Data Location**: the name of the data location where the model is deployed.
    - **Datasource**: the name of the datasource, as defined in the Configuration interface.
    - **Instance URL**: the URL of the Data Management instance.
    - **Root Folder**: the path to the folder containing the SEML design file for the model you intend to deploy. For example:
    ```
    my-data-product/src/my-model
    ```
