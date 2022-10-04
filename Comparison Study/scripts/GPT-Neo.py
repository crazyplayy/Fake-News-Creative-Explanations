from transformers import pipeline # First line

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # Second line

prompt = "Write me a poem for a given summary taking into account the claim and the label     Claim: The US has made strides in reducing carbon emissions that other parts of the world have not.   Label: true   Summary Explanation:    When it comes to greenhouse gas emissions, the United States has made progress, decreasing emissions 8.2% from 2010 to 2019.   Among other  top emitters, Brazil made the most progress for that time period, with an emission decrease of 31.3%, but is now on the rise.   But China and India saw major increases, of 25.4% and 36.6% respectively.   Poem:    Co2, our little “Frienemy”,  you and the other greenhouse gases  need to leave, desperately!    The US set an example for once,  decreasing their emissions 8.2%  Brazil follows their example, but are struggling with the maintenance,  while China and India counter the occident.       Claim:  Taxpayers spent $70,000,000 to develop this drug ( remdesivir).    Label: true   Summary Explanation:    When the drug that would come to be known as remdesivir was identified as a possible treatment for the Ebola virus, the Department of Defense paid Gilead to develop it, to the tune of $34.5 million today  A $6 million grant from the National Institutes of Health was awarded to researchers at the University of North Carolina to speed the development of remdesivir  NIH also sunk $30 million into the clinical trial to observe how remdesivir acted against COVID-19 earlier this spring  Both the Department of Defense and NIH are federal agencies whose budgets stem from tax dollars     Poem:         " # Third line

res = generator(prompt, max_length=1150, do_sample=True, temperature=0.9) # Fourth line

print(res[0]['generated_text'])

with open('gpttext.txt', 'w') as f:
    f.writelines(res[0]['generated_text'])