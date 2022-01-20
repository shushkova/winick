import flair
from flair.data import Corpus
from flair.datasets import TREC_6
from flair.trainers import ModelTrainer
import flair.models.text_classification_model as tc
from flair.models import TARSClassifier
from flair.data import Sentence

loaded = TARSClassifier.load('resources/best-model.pt')

candidate_labels = ['Dinner Parties', 'Pleasing A Crowd', 'Wine And Cheese Night',
                    'White Wine Lovers Craving Red', 'Dinner With The Parents',
                    'Host/Hostess Gifting', 'Party Wine', 'Relaxing After Work',
                    'House Wine', 'Summer Sipping', 'Weekday Dinner Pairings',
                    'Sounding Like A Wine Pro', "Treat Yo'self",
                    'Last Minute Wine Runs', 'Feeling Natural', 'Date Night',
                    'Chilled Red Cravings', 'Picnics In The Park', 'Wine Cocktails',
                    'Winning Over the Boss', 'End of Day Sipping',
                    'Impressing On A Budget', 'Holiday Meals', 'Popping Bottles',
                    'All-Day Sipping', 'Sipping Without Food',
                    'Drinking Outside the Lines', 'Backyard BBQs', 'Boozy Beach Trips',
                    'Penny Pinching', 'Pizza Night', 'Take-Out Night', 'Steak Dinner',
                    'Happy Hour', 'Netflix And Chill', 'Special Occasion Splurges',
                    'Asian Food', 'Brunch Sipping', 'Starting The Night',
                    'Cooking And Sipping', 'Indian Food', 'Taco Tuesday', 'Day Trips',
                    'Cold Weather Hibernation', 'Long-Term Aging', 'Rosé All Day',
                    'Sweet Tooth Cravings', 'Spicy Pairings',
                    'Winter White Wine Drinking', 'Red Wine Lovers Craving White']


async def predict(message):
    sequence_to_classify = message

    s = Sentence(sequence_to_classify)
    loaded.predict_zero_shot(s, candidate_labels)
    predicted_values = [i['value'] for i in
                        sorted(s.to_dict()['labels'], key=lambda k: k['confidence'], reverse=True)[:3]]
    return ', '.join(predicted_values)
