import spacy
from spacy.language import Language
from spacy.tokens import Doc

class SpacyNLPProcessor:
    def __init__(self, model="en_core_web_sm"):
        """
        Initialize the SpacyNLPProcessor with a specified language model.
        """
        self.nlp = spacy.load(model)
        self.components = []

    def process_text(self, text):
        """
        Process text with spaCy, performing tokenization, POS tagging, NER, and dependency parsing.
        """
        return self.nlp(text)

    @staticmethod
    @Language.component('extract_named_entities')
    def extract_named_entities(doc):
        """
        Extract named entities from the processed text.
        """
        entities =  [(ent.text, ent.label_) for ent in doc.ents]
        doc._.entities = entities
        return doc
    
    @staticmethod
    @Language.component('pos_tagging')
    def pos_tagging(doc):
        """
        Extract Part-of-Speech (POS) tags from the processed text.
        """
        pos_tags =  [(token.text, token.pos_) for token in doc]
        doc._.pos_tags = pos_tags
        return doc

    @staticmethod
    @Language.component('dependency_parsing')
    def dependency_parsing(doc):
        """
        Extract dependency parsing information from the processed text.
        """
        dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
        doc._.dependencies = dependencies
        return doc 

    def custom_pipeline(self, text):
        """
        Example of a custom processing pipeline that includes multiple NLP tasks.
        """
        doc = self.process_text(text)
        entities = self.extract_named_entities(doc)
        pos_tags = self.pos_tagging(doc)
        # dependencies = self.dependency_parsing(doc)

        return {
            'entities': entities,
            'pos_tags': pos_tags,
            # 'dependencies': dependencies,
        }

    def add_custom_component(self, component):
        """
        Add a custom component to the spaCy pipeline.
        """
        self.nlp.add_pipe(component)
        self.components.append(component)

    def save_model(self, output_dir):
        """
        Save the spaCy model to a directory for later use.
        """
        self.nlp.to_disk(output_dir)

    def load_model(self, model_dir):
        """
        Load a spaCy model from a directory.
        """
        self.nlp = spacy.load(model_dir)


# Example usage
# if __name__ == "__main__":
#     text = "Apple is looking at buying U.K. startup for $1 billion."

#     processor = SpacyNLPProcessor()
#     # processed_data = processor.custom_pipeline(text)

#     # Create custom attributes for the Doc object
#     if not Doc.has_extension("entities"):
#         Doc.set_extension("entities", default=None)
#     if not Doc.has_extension("pos_tags"):
#         Doc.set_extension("pos_tags", default=None)
#     if not Doc.has_extension("dependencies"):
#         Doc.set_extension("dependencies", default=None)
#     #add components to the pipeline
#     processor.add_custom_component("extract_named_entities")    
#     processor.add_custom_component("pos_tagging")
#     processor.add_custom_component("dependency_parsing")
#     # processed_data = processor.nlp(text)
#     processed_data = processor.process_text(text)

#     pipeline_data = {
#         'text': processed_data.text,
#         'entities': processed_data._.entities,
#         'pos_tags': processed_data._.pos_tags,
#         'dependencies': processed_data._.dependencies,
#     }
    


#     print("Entities:", pipeline_data['entities'])
#     print("POS Tags:", pipeline_data['pos_tags'])
#     print("Dependencies:", pipeline_data['dependencies'])
#     # print(dependencies)
