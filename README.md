### Assignment 2 Codes ###

To run the codes for part 1, simply install python 3.10, and enter into the 
virtual environment for the project using the command :

`source ./.venv/bin/activate`

After doing this, be sure that all of the necessary packages are installed
by running : 

`pip install -r requirements.txt`

Then, enter into the Part 1 directory like : 

`cd Part\ 1`

and run the code as such : 

`python ./reverse.py`

This will start a procedure that will determine the AES key from the final
round key (K11), and then use this to decrypt the captured ciphertext.