#http://mohitmayank.com/a_lazy_data_science_guide/natural_language_processing/T5/#t5-finetuning 

from transformers import T5Tokenizer, T5Model #T5ForConditionalGeneration

model = T5Model.from_pretrained("t5-3b")
tokenizer = T5Tokenizer.from_pretrained("t5-3b")

input_ids = tokenizer(
    "Write me a poem for a given summary taking into account the claim and the label     Claim: The US has made strides in reducing carbon emissions that other parts of the world have not.   Label: true   Summary Explanation:    When it comes to greenhouse gas emissions, the United States has made progress, decreasing emissions 8.2% from 2010 to 2019.   Among other  top emitters, Brazil made the most progress for that time period, with an emission decrease of 31.3%, but is now on the rise.   But China and India saw major increases, of 25.4% and 36.6% respectively.   Poem:    Co2, our little “Frienemy”,  you and the other greenhouse gases  need to leave, desperately!    The US set an example for once,  decreasing their emissions 8.2%  Brazil follows their example, but are struggling with the maintenance,  while China and India counter the occident.       ", return_tensors="pt"
).input_ids     

decoder_input_ids = tokenizer("Claim:  Taxpayers spent $70,000,000 to develop this drug ( remdesivir).    Label: true   Summary Explanation:    When the drug that would come to be known as remdesivir was identified as a possible treatment for the Ebola virus, the Department of Defense paid Gilead to develop it, to the tune of $34.5 million today  A $6 million grant from the National Institutes of Health was awarded to researchers at the University of North Carolina to speed the development of remdesivir  NIH also sunk $30 million into the clinical trial to observe how remdesivir acted against COVID-19 earlier this spring  Both the Department of Defense and NIH are federal agencies whose budgets stem from tax dollars     Poem:    ", return_tensors="pt").input_ids  # Batch size 1

outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
last_hidden_states = outputs.last_hidden_state
#outputs = model.generate(input_ids, max_new_tokens=2000)

#print(tokenizer.decode(outputs[0], skip_special_tokens=True))