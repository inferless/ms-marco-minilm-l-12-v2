from sentence_transformers import CrossEncoder

class InferlessPythonModel:
    def initialize(self):
        self.model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2', max_length=512,device="cuda")

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
