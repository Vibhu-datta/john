class MadLibs:

    #create sentence with blanks
    def __init__(self):
        self.sentence = "Flip-flops are a staple of any ____ summer wardrobe."
        pass
    #each blank is labled with the word type to fil it in with
    #take players input on what to fill in the blanks with 
    def get_user_input(self):
        print(self.sentence)
        self.word = input("type an adjective: ")
   #print sentence replacing the blanks with players input     
    def show_new_sentence(self):
        print(self.sentence.replace("____", self.word))







    
my_mad_libs = MadLibs()
my_mad_libs.get_user_input()
my_mad_libs.show_new_sentence()
