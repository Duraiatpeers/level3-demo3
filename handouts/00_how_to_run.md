# How to run the programs

1. Start the PX Service Assistant app. Use the version your trainer gave you for this module. It must be running on `http://localhost:8000`.
2. Set these in PowerShell, in the terminal you will run the programs from. The app needs your own
   Azure OpenAI chat deployment, so you supply the endpoint, the key and the deployment name:

   ```
   setx MODEL_ENDPOINT "https://YOUR-RESOURCE.services.ai.azure.com/"
   setx MODEL_KEY "your Azure OpenAI key"
   setx MODEL_DEPLOYMENT "your chat deployment name"
   setx PX_API_KEY "the key your trainer gave you"      # skip if your trainer gave you no key
   ```

   Where to find them: in the Azure portal, open your Azure OpenAI resource, click **Keys and
   Endpoint**, and copy **Endpoint** and **KEY 1**. For the deployment name, open the resource in
   **Azure AI Foundry**, click **Deployments**, and copy the **Name** column of your chat
   deployment - the name you gave it, not the model name underneath.

   `setx` stores the values for good but only applies to **new** terminals, so close this one and
   open a fresh one. For this terminal only, use `$env:MODEL_KEY = "..."` instead, one per line.

   Keep two terminals open: one runs the app, the other runs these programs.

3. Check your setup before anything else:

   `python 00_check_setup.py`

   It prints your variables and makes one request. Do not go on until it says `Status: 200`.
   `KeyError: 'MODEL_KEY'` means that variable is not set in this terminal.

4. From the `programs` folder, run a program:

   `python 01_one_timing.py`

5. Run the test file with pytest:

   `python -m pytest 10_cost_regression_test.py -v`

What is new in this module:
- The app now returns two extra things with every answer: `latency_ms` (how long the answer took, in milliseconds) and `usage` (how many tokens the model read and wrote).
- Some programs send many requests at once. They use the shared model quota. Run them as your trainer says, and do not raise the numbers on your own.

If something looks wrong:
- Every run says "No answer returned": run `python 01_one_timing.py` and read the status line. A 502 can mean a filter stopped the request or the model was throttled. A connection error means the app is not running.
- `KeyError: 'usage'`: your app is the older version. Ask your trainer for the app with the usage change.
- Numbers differ from your neighbour's: normal. Model speed changes from run to run.
