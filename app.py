from sentence_transformers import CrossEncoder

class InferlessPythonModel:
    def initialize(self):
        self.model = CrossEncoder('model_name', max_length=512)

    def infer(self, inputs):
        data_pairs = inputs["data_pairs"]
        scores = self.model.predict(data_pairs)
        return {"result": scores}
    def finalize(self, args):
        self.pipe = None
