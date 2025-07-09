## Retab Plugin

### Credentials

The Retab API key is required (https://docs.retab.com/overview/quickstart)

### Tools

#### 1. Retab Extraction (`retab`)
Tool that utilizes Retab to extract information from documents.

**Arguments:**
- `json_schema` (`string`, required): JSON schema defining the expected data structure.
- `model` (`string`, required): The model to use for extraction.
- `document` (`file`, required): The document to be extracted.
- `modality` (`select`, required): The modality of the document. Options: `native`, `image`, `text`, `image+text`.
- `image_resolution_dpi` (`number`, optional): The resolution the image is scanned at.
- `browser_canvas` (`select`, optional): The canvas size of the browser. Options: `A3`, `A4`, `A5`.
- `temperature` (`number`, optional): The temperature of the model.
- `n_consensus` (`number`, optional): The number of consensus extractions to perform.
- `reasoning_effort` (`select`, optional): The effort level for the model to reason about the input data. Options: `low`, `medium`, `high`.


#### 2. Retab Parsing (`retab_parse`)
Tool that utilizes Retab to parse documents into an LLM-friendly format.

**Arguments:**
- `model` (`string`, required): The model to use for extraction.
- `document` (`file`, required): The document to be extracted.
- `image_resolution_dpi` (`number`, optional): The resolution the image is scanned at.
- `browser_canvas` (`select`, optional): The canvas size of the browser. Options: `A3`, `A4`, `A5`.
- `table_parsing_format` (`select`, optional): The format to parse tables into. Options: `markdown`, `yaml`, `html`, `json`.

#### Other
Github repository: https://github.com/retab-dev/dify
Contact: sacha@retab.com
