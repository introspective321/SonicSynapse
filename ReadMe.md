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


----------------------------------------------------
Data columns (total 21 columns):
    Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   track_id             50683 non-null  object 
 1   name                 50683 non-null  object 
 2   artist               50683 non-null  object 
 3   spotify_preview_url  50683 non-null  object 
 4   spotify_id           50683 non-null  object 
 5   tags                 49556 non-null  object 
 6   genre                22348 non-null  object 
 7   year                 50683 non-null  int64  
 8   duration_ms          50683 non-null  int64  
 9   danceability         50683 non-null  float64
 10  energy               50683 non-null  float64
 11  key                  50683 non-null  int64  
 12  loudness             50683 non-null  float64
 13  mode                 50683 non-null  int64  
 14  speechiness          50683 non-null  float64
 15  acousticness         50683 non-null  float64
 16  instrumentalness     50683 non-null  float64
 17  liveness             50683 non-null  float64
 18  valence              50683 non-null  float64
 19  tempo                50683 non-null  float64
 20  time_signature       50683 non-null  int64  
dtypes: float64(9), int64(5), object(7)
