## Retab Plugin

### Credentials

The Retab API key is required (https://docs.retab.com/overview/quickstart)

### Tools

#### 1. Retab Extraction (`retab`)
Tool that utilizes Retab to extract information from documents using a certain iteration within a project.

**Arguments:**
- project_id: String - The ID of the project with which to extract the document. (Required)
- iteration_id: String - The ID of the iteration with which to extract the document. (Required)
- documents: Array[File] - The documents to be extracted. This should be an array of files. (Required)
- temperature: Number - The temperature of the model, which can influence the randomness of the extraction. (Optional)
- seed: Number - The seed value for the extraction, used for reproducibility. (Optional)


#### Other
Github repository: https://github.com/retab-dev/dify
Contact: sacha@retab.com
