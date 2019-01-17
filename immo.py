#This is a simulation of immo key that has a transponder chip in it. The chip has a key
#ID that is stored in an encrypted format
class Transponder:
    def __init__(self):
        self.key_id_transponder = "abcdefghi"   #key ID of the transponder key

    #when the Immo control module asks for the transponder key the corresponding key is transmitted
    def request_key_ID_transponder(self):
        return self.key_id_transponder

#Powertrain control Module controls the engine functionality, it has 2 keys, one called the key ID
#to authenticate the key and another called code to authenticate the Immo control model
class PCM:
    def __init__(self):
        self.key_id_PCM = "xyzabc" #Key ID stored in PCM
        self.code_PCM = "SteveJobs" #Code stored in the PCM

    #get the value of key ID stored in PCM
    def request_ID_PCM(self):
        return self.key_id_PCM
    #get the Code value stored in PCM
    def request_code_PCM(self):
        return self.code_PCM

#Immo Controller is the main computing unit of the Immo. It has the key ID of both transponder and PCM
#and also code of the PCM
class ImmoController:
    def __init__(self):
        self.key_id_trans_icm = "abcdefghi" #key id of transponder stored in ICM
        self.code_icm = "SteveJobs" #code of PCM stored in ICM
        self.key_id_icm_PCM = "xyzabc" #Key id of PCM stored in ICM
        self.key_verify_trans = False #flag for transpomnder key verification
        self.key_verify_PCM = False #flag for PCM key verification
        self.code_verify = False #flag for the PCM code verification

    #if the KeyID of the transponder and the key id of the ICM matches then verify
    def verify_key_ID_transponder(self):
        if(self.key_id_trans_icm == self.key_id_transponder):
            self.key_verify_trans = True

    #if KeyID of the PCM and the key ID of the ICM matches then verify
    def verify_key_ID_PCM(self):
        if(self.key_id_icm_PCM == self.key_id_PCM):
            self.key_verify_PCM = True

    #if the code of the icm and the PCM verify then return true
    def verify_code(self):
        if(self.code_icm == self.code_PCM):
            self.code_verify = True

    #Engine start routine
    def start_engine(self):
        pass

    #incase of non authenticity abort the engine start operation
    def stop_engine(self):
        pass

    # the initial function when the key is put to the key slot
    def key_insert(self):
        transponder_instance = Transponder() #the transponder is initialised
        self.key_id_transponder = transponder_instance.request_key_ID_transponder() #Key is requested from transponder
        self.verify_key_ID_transponder()#The key is verified

        if(self.key_verify_trans == False): #if the key verification fail
            print("Invalid Key in the key socket!!")
            print("Engine start aborted !")
            self.stop_engine() #abort the engine start operation
        else:#now authenticate PCM
            PCM_instance = PCM() #create an Instance of PCM
            self.key_id_PCM = PCM_instance.request_ID_PCM()#request for the key of PCM
            self.code_PCM = PCM_instance.request_code_PCM()#request for the code of PCM
            self.verify_key_ID_PCM() #verify the key of PCM
            self.verify_code() #verify the code of PCM
            if(self.key_verify_PCM and self.code_verify): #if both PCM key and code are authenicated start the engine
                print("Engine is starting......")
                print("Engine is up and running!!")
                self.start_engine() #start the engine
            else:
                print("Invalid ICM code or key!!") #authentication failed. Abort the engine start
                self.stop_engine()

if __name__ == "__main__":
    immo_instance = ImmoController() #initailise the immo contoller
    immo_instance.key_insert() #insert the key to the key holder to start the engine
