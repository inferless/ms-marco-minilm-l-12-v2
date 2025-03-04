import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
from sentence_transformers import CrossEncoder

class InferlessPythonModel:
    def initialize(self):
        model_id = 'cross-encoder/ms-marco-MiniLM-L-12-v2'
        snapshot_download(repo_id=model_id,allow_patterns=["*.safetensors"])
        self.model = CrossEncoder(model_id, max_length=512,device="cuda")

    def infer(self, inputs):
        query = inputs["query"]
        paragraphs = inputs["paragraphs"]
        data_pairs = []
        for paragraph in paragraphs:
            data_pairs.append((query,paragraph))
        scores = self.model.predict(data_pairs)
        return {"result": scores}
    def finalize(self, args):
        self.pipe = None
