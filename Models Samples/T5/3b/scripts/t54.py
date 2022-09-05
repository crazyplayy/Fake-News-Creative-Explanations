from transformers import T5ForConditionalGeneration, T5Tokenizer

import torch
torch.set_default_tensor_type(torch.cuda.FloatTensor)


    
guardar = "t54.txt"

tokenizer = T5Tokenizer.from_pretrained("t5-3b")
model = T5ForConditionalGeneration.from_pretrained("t5-3b")

input_ids = tokenizer.encode(
    "Write me a poem for a given summary taking into account the claim and the label     Claim:  The second booster has eight strains of HIV.    Label: pants-fire   Summary Explanation:     The ingredients of COVID-19 vaccines are published and do not include HIV.   The vaccine ingredients do not change between doses. Each shot in the mRNA COVID-19 vaccine series, including the booster, has the same ingredients.      Poem:    Every food has recipes,  precious holy grails,  Vaccines fight enemies,  who run off with their tails.    You don't change instructions,  just because the dose is new.  We already made the introductions,  why would HIV be in queue?       Claim: Ukraine was the No. 1 donor to Hillary Clinton when she was running for president.     Label: false   Summary Explanation:    Hillary Clinton’s 2016 presidential campaign did not report receiving any donations from the Ukrainian government or Ukrainian nationals. Those donations would have been illegal.  A spokesperson for Marjorie Taylor Greene cited a 2015 Wall Street Journal graphic that has been frequently misrepresented online. The chart shows donations to the Clinton Foundation between 1999 and 2014 by the nationality of the individuals who made them; it does not say anything about donations to the foundation by foreign governments.   The Clinton Foundation said it has never received donations from Ukraine’s government.   Poem:    In 2016, Hillary ran for president,  No reports of donations from Ukraine were evident.  Those donations would’ve been illegal,  Truthful reports would’ve been a miracle.  Graphics misrepresented,  Can affect one’s reputation,  Clinton Foundation received individual donations  Never from Ukraine’s government,  That was an incident.       Claim: Says Joe Biden risks war with Russia because Vladimir Putin doesn’t “believe in transgender rights.“   Label: pants-fire   Summary Explanation:    Ohio Senate candidate JD Vance said the State Department’s focus on transgender rights is inflaming the conflict with Russia in Ukraine.  Russia has placed as many as 150,000 troops near Ukraine’s borders.  Russia has said Ukraine’s ties to NATO are a key threat to Russia’s national security.   Poem:    Nato is a threat for Putin,   almost as transgenders are for JD Vance.  150,000 troops near the borders?  it’s fair to assume one in charge has a disorder.  Transgender or cisgender,  doesn’t define an offender.   Biden claims Ukraine’s safety,  Putin’s heart only knows obscurity.       Claim:  Map shows states where all of the children… are back to living mask-free, normal lives.    Label: barely-true   Summary Explanation:     Though the majority of states do not have statewide school mask mandates, individual school districts still have mandates.    The absence of state mask rules has not meant a full return to pre-pandemic “normal” at school in most places.     Poem:    We all want the same,  to go back to normality,  but like this claim,  that's still not the reality.    The majority of states,  do not have statewide   school mask mandates.  However,   individual school districts abide  since they still have mandates.    If mask rules evaporated,  that doesn't mean  normality would be stated  in most schools scene.       Claim:  Children are almost immune from this disease.    Label: false   Summary Explanation:    Children represent about 7.3% of COVID-19 cases in the U.S and less than 0.1% of deaths, according to the CDC.  Many children were not exposed to the virus as much as adults because schools shut down nationwide in March.  Research in other countries that reopened schools shows children can catch COVID-19.     Poem:", return_tensors="pt", truncation=True
) 

print("tou a gerar a sample ")
greedy_output = model.generate(input_ids, min_length=300, max_length=2000)

print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

with open(guardar, 'w') as f:
    f.writelines(tokenizer.decode(greedy_output[0], skip_special_tokens=True))