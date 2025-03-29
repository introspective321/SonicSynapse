# Deep Learning (CSL4020)
## Course Project
----------------------------------------------------
A deep learning-based system for voice-controlled music recommendation.


-----------------------------------------------------------------------------
 Voice to text: pretrained model like whisper
    * This will give us the text.

Now we tokenize this, pass it through a LSTM/Transformer to get "Text Embedding" 1 
------------------------------------------------------------------------------
Now, if we need the audio features as well, say tone, energy, speed:
    * CNN needed for this to get an "emotion vector" (dimensions need to be decided)

Here CNN will take audio as input (need to think about it)
---------------------------------------------------------------------------------
 
We then concatenate the "Text Embedding" + "Emotion Vector"
Then pass this through dense layer(s) to get the final user command embedding

--------------------------------------------------------------------------
 Music recommendation



 Last.fm

 Ravedness (Audio part) 



