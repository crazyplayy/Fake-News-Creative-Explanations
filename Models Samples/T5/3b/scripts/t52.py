from transformers import T5ForConditionalGeneration, T5Tokenizer

import torch
torch.set_default_tensor_type(torch.cuda.FloatTensor)


    
guardar = "t52.txt"

tokenizer = T5Tokenizer.from_pretrained("t5-3b")
model = T5ForConditionalGeneration.from_pretrained("t5-3b")

input_ids = tokenizer.encode(
    "Write me a poem for a given summary taking into account the claim and the label     Claim:  The New York City Police Department arrested a 9-year-old because she didn’t have a vaccine card in the museum.    Label: false   Summary Explanation:     The 9-year-old was not arrested. She was escorted to the police station in a separate car from those who were arrested — a group which included her mother — and cared for by police officers until her mother was released.    The adults were arrested and charged with trespassing because they would not leave the museum after it closed.     Poem:    Kids like to fool around  making jokes and pranks,  but they are not robbing banks  in a museum, goons ain't found.    This kid was escorted  to the police station,  there she was supported  and cared with attention.    She ended up there,  because mom was in a group  that police arrested fair.  The museum floor needs to be swoop  Time's over for photos and stare.    COVID-19 or card vaccine,  have no part in this.  Manipulation is no sin,  but trespassing is.       Claim:  Map shows states where all of the children… are back to living mask-free, normal lives.    Label: barely-true   Summary Explanation:     Though the majority of states do not have statewide school mask mandates, individual school districts still have mandates.    The absence of state mask rules has not meant a full return to pre-pandemic “normal” at school in most places.     Poem:    We all want the same,  to go back to normality,  but like this claim,  that's still not the reality.    The majority of states,  do not have statewide   school mask mandates.  However,   individual school districts abide  since they still have mandates.    If mask rules evaporated,  that doesn't mean  normality would be stated  in most schools scene.       Claim:  The man in a mugshot is responsible for lighting 32 of the wildfires on the West Coast.    Label: false   Summary Explanation:    The man in the photo, Brandon McGlover, did not light 32 wildfires, in 2020 or any other year.  McGlover was arrested in July 2018 and is currently in prison for lighting nine fires in southwest California, including the Cranston Fire, which forced thousands of evacuations and burned over 13,000 acres.  Experts say that climate change has modified environments in the West Coast, making them more conducive to wildfires. ​     Poem:", return_tensors="pt", truncation=True
) 

print("tou a gerar a sample ")
greedy_output = model.generate(input_ids, min_length=300, max_length=2000)

print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

with open(guardar, 'w') as f:
    f.writelines(tokenizer.decode(greedy_output[0], skip_special_tokens=True))