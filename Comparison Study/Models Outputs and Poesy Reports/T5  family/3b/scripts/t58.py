from transformers import T5ForConditionalGeneration, T5Tokenizer

import torch
torch.set_default_tensor_type(torch.cuda.FloatTensor)


    
guardar = "t58.txt"

tokenizer = T5Tokenizer.from_pretrained("t5-3b")
model = T5ForConditionalGeneration.from_pretrained("t5-3b")

input_ids = tokenizer.encode(
    "Write me a poem for a given summary taking into account the claim and the label     Claim:  The second booster has eight strains of HIV.    Label: pants-fire   Summary Explanation:     The ingredients of COVID-19 vaccines are published and do not include HIV.   The vaccine ingredients do not change between doses. Each shot in the mRNA COVID-19 vaccine series, including the booster, has the same ingredients.      Poem:    Every food has recipes,  precious holy grails,  Vaccines fight enemies,  who run off with their tails.    You don't change instructions,  just because the dose is new.  We already made the introductions,  why would HIV be in queue?       Claim:  Map shows states where all of the children… are back to living mask-free, normal lives.    Label: barely-true   Summary Explanation:     Though the majority of states do not have statewide school mask mandates, individual school districts still have mandates.    The absence of state mask rules has not meant a full return to pre-pandemic “normal” at school in most places.     Poem:    We all want the same,  to go back to normality,  but like this claim,  that's still not the reality.    The majority of states,  do not have statewide   school mask mandates.  However,   individual school districts abide  since they still have mandates.    If mask rules evaporated,  that doesn't mean  normality would be stated  in most schools scene.       Claim: Ukraine was the No. 1 donor to Hillary Clinton when she was running for president.     Label: false   Summary Explanation:    Hillary Clinton’s 2016 presidential campaign did not report receiving any donations from the Ukrainian government or Ukrainian nationals. Those donations would have been illegal.  A spokesperson for Marjorie Taylor Greene cited a 2015 Wall Street Journal graphic that has been frequently misrepresented online. The chart shows donations to the Clinton Foundation between 1999 and 2014 by the nationality of the individuals who made them; it does not say anything about donations to the foundation by foreign governments.   The Clinton Foundation said it has never received donations from Ukraine’s government.   Poem:    In 2016, Hillary ran for president,  No reports of donations from Ukraine were evident.  Those donations would’ve been illegal,  Truthful reports would’ve been a miracle.  Graphics misrepresented,  Can affect one’s reputation,  Clinton Foundation received individual donations  Never from Ukraine’s government,  That was an incident.       Claim: Says Joe Biden risks war with Russia because Vladimir Putin doesn’t “believe in transgender rights.“   Label: pants-fire   Summary Explanation:    Ohio Senate candidate JD Vance said the State Department’s focus on transgender rights is inflaming the conflict with Russia in Ukraine.  Russia has placed as many as 150,000 troops near Ukraine’s borders.  Russia has said Ukraine’s ties to NATO are a key threat to Russia’s national security.   Poem:    Nato is a threat for Putin,   almost as transgenders are for JD Vance.  150,000 troops near the borders?  it’s fair to assume one in charge has a disorder.  Transgender or cisgender,  doesn’t define an offender.   Biden claims Ukraine’s safety,  Putin’s heart only knows obscurity.       Claim: The US has made strides in reducing carbon emissions that other parts of the world have not.   Label: true   Summary Explanation:    When it comes to greenhouse gas emissions, the United States has made progress, decreasing emissions 8.2% from 2010 to 2019.   Among other  top emitters, Brazil made the most progress for that time period, with an emission decrease of 31.3%, but is now on the rise.   But China and India saw major increases, of 25.4% and 36.6% respectively.   Poem:    Co2, our little “Frienemy”,  you and the other greenhouse gases  need to leave, desperately!    The US set an example for once,  decreasing their emissions 8.2%  Brazil follows their example, but are struggling with the maintenance,  while China and India counter the occident.       Claim:  The New York City Police Department arrested a 9-year-old because she didn’t have a vaccine card in the museum.    Label: false   Summary Explanation:     The 9-year-old was not arrested. She was escorted to the police station in a separate car from those who were arrested — a group which included her mother — and cared for by police officers until her mother was released.    The adults were arrested and charged with trespassing because they would not leave the museum after it closed.     Poem:    Kids like to fool around  making jokes and pranks,  but they are not robbing banks  in a museum, goons ain't found.    This kid was escorted  to the police station,  there she was supported  and cared with attention.    She ended up there,  because mom was in a group  that police arrested fair.  The museum floor needs to be swoop  Time's over for photos and stare.    COVID-19 or card vaccine,  have no part in this.  Manipulation is no sin,  but trespassing is.       Claim: Bill Gates hatches 'horribly stupid' plan to block out the sun   Label: false   Summary Explanation:    Harvard researchers proposed a small-scale experiment that would spray aerosols into the atmosphere to reflect some sunlight back into space, a technology aimed at minimizing global warming. The experiment would measure the risks and effectiveness of the technology.  The experiment is funded in part through Harvard’s Solar Geoengineering Research Program, and Bill Gates is among the donors to that program.  The claim first surfaced in 2021 and has been previously debunked.   Poem:    yeah is hot,  glaciers are no longer in stock,  Bill Gates a solution tried to find,  but block only works on intagram, bear this in mind.    Now, the true story,  Bill, you don´t deserver the glory!  Havard was the one, the original author  You only gave them money and they took the offer.       Claim: Russia has never attacked anyone throughout its history.   Label: pants-fire   Summary Explanation:    Historians cite upwards of a dozen examples dating back to the 1500s in which Russia or the Soviet Union attacked another country without being militarily attacked first.   Russia may offer various justifications for why it attacked another country in these instances, but each of these examples involved militarily unprovoked actions by Russia or the Soviet Union.    Poem:    Soviet Union or Russia,  the tale is old as time.   Historians carry examples,  Russians justifications  But all we see is crime.  Justifications filled with temptations,   military attacks cause obliterations.       Claim:  Says President Donald Trump never downplayed the virus.    Label: pants-fire   Summary Explanation:    Between the end of January and mid March, Trump told the public that the virus was well under control and presented little risk.  He told Bob Woodward that he played down the virus to avoid creating panic.     Poem:", return_tensors="pt", truncation=True
) 

print("tou a gerar a sample ")
greedy_output = model.generate(input_ids, min_length=300, max_length=2000)

print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

with open(guardar, 'w') as f:
    f.writelines(tokenizer.decode(greedy_output[0], skip_special_tokens=True))