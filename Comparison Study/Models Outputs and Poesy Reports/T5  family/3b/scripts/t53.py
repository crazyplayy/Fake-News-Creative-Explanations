from transformers import T5ForConditionalGeneration, T5Tokenizer

import torch
torch.set_default_tensor_type(torch.cuda.FloatTensor)


    
guardar = "t53.txt"

tokenizer = T5Tokenizer.from_pretrained("t5-3b")
model = T5ForConditionalGeneration.from_pretrained("t5-3b")

input_ids = tokenizer.encode(
    "Write me a poem for a given summary taking into account the claim and the label     Claim:  The second booster has eight strains of HIV.    Label: pants-fire   Summary Explanation:     The ingredients of COVID-19 vaccines are published and do not include HIV.   The vaccine ingredients do not change between doses. Each shot in the mRNA COVID-19 vaccine series, including the booster, has the same ingredients.      Poem:    Every food has recipes,  precious holy grails,  Vaccines fight enemies,  who run off with their tails.    You don't change instructions,  just because the dose is new.  We already made the introductions,  why would HIV be in queue?       Claim: Says Joe Biden risks war with Russia because Vladimir Putin doesn’t “believe in transgender rights.“   Label: pants-fire   Summary Explanation:    Ohio Senate candidate JD Vance said the State Department’s focus on transgender rights is inflaming the conflict with Russia in Ukraine.  Russia has placed as many as 150,000 troops near Ukraine’s borders.  Russia has said Ukraine’s ties to NATO are a key threat to Russia’s national security.   Poem:    Nato is a threat for Putin,   almost as transgenders are for JD Vance.  150,000 troops near the borders?  it’s fair to assume one in charge has a disorder.  Transgender or cisgender,  doesn’t define an offender.   Biden claims Ukraine’s safety,  Putin’s heart only knows obscurity.       Claim: The US has made strides in reducing carbon emissions that other parts of the world have not.   Label: true   Summary Explanation:    When it comes to greenhouse gas emissions, the United States has made progress, decreasing emissions 8.2% from 2010 to 2019.   Among other  top emitters, Brazil made the most progress for that time period, with an emission decrease of 31.3%, but is now on the rise.   But China and India saw major increases, of 25.4% and 36.6% respectively.   Poem:    Co2, our little “Frienemy”,  you and the other greenhouse gases  need to leave, desperately!    The US set an example for once,  decreasing their emissions 8.2%  Brazil follows their example, but are struggling with the maintenance,  while China and India counter the occident.       Claim:  An audio message lists five ways people can prevent the novel coronavirus.    Label: false   Summary Explanation:    An audio message lists 10 ways people can avoid contracting COVID-19. We fact-checked five of the most questionable claims.  There is no evidence that sipping water every 20 minutes or exposing your clothing to the sun can help prevent the coronavirus.  Officials advise people to wash their hands, but not every 20 minutes, as the message claims. There’s also no evidence that consuming cold things makes you more susceptible to the virus.  There’s no proof that the coronavirus can live for up to nine days on metallic surfaces. A preliminary study suggests it can remain viable on stainless steel for up to three days.     Poem:", return_tensors="pt", truncation=True
) 

print("tou a gerar a sample ")
greedy_output = model.generate(input_ids, min_length=300, max_length=2000)

print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

with open(guardar, 'w') as f:
    f.writelines(tokenizer.decode(greedy_output[0], skip_special_tokens=True))