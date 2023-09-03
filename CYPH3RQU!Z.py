#Cyph3rQuiz
#This program is a short knowledge based quiz on the different encryption methods

print('Hi! Welcome to my Encyption Quiz!')
print('')

#Ask user if they was to continue with game
play_game= input('Would you like to play? ')
if play_game.lower() != 'yes':
    print('End of program, Bye!')
    quit()

print('')
print('Let\'s Go! Enter Corresponding letter for each answer. Example, type "a" ')    
print('')

#Questions asked if incorrect, prints the correct answer
question = str(input('1. Does symmetric encryption use a single shared key to encrpyt and decrypt? \nA. true \nB. false \n'))
if question.lower() == 'a': 
    print('Correct!')
else:
    print('Symmetric encrpytion uses a single shared key, Asymmetric encryption uses 2 or more keys.')
    
question= str(input('2. Which encryption uses more overhead such as CPU, storage and resoruces? \nA. Symmetric encryption \nB. Elliptic curve cryptography \nC. Asymmetric encryption \n'))
if question.lower() == 'c':
    print('Right on!')
else:
    print('4. Asymmetric Keys use more resources due to mathematically related key generation that builds both public and private keys simultaneously using randomization and prime numbers.')
    
question= str(input('3. The type of encryption that uses curves instead of numbers, usually has smaller keys for IoT devices and mobile devices/applications. \nA. Homomorphic encryption \nB. Elliptic curve cryptography \nC. Crytographic Keys\n'))
if question.lower() == 'b':
    print('Yeaaaa!!')
else:
    print('Sorry. Elliptic curve cryptography allows you to use asymmetric cryptography but employs curves for smaller keys,storage and transmissions.')

question= str(input('4. Is this Asymmetric encryption example correct? (Type: A. Yes or B. No) \n Jacob types an email and needs to send it to Monica. He types it in plain text but uses Monica\'s public key to encrpyt and create a ciphertext, then sends the email. Monica receives the email and uses her private key to decrypt the ciphertext into the original plain text.\n'))
if question.lower() == 'a':
    print('Correct!')
else:
    print('Incorrect. This example demonstrates the use of asymmetric Encryption')

question= str(input('5. MD5 is a hash found to have collision vulnerabilities. \nA. true \nB. false\n'))
if question.lower() == 'a':
    print('Right on')
else:
    print('Sorry. MD5 causes hash collisions and should not be used as hash algorithm')

print('')
question= str(input('6. A type of block cipher that uses an Initialization Vector and a cipher encryption to create ciphertext. That same ciphertext is then used for the next encrypted block and an IV. This method is usually known for the plain text block being XORed with the previous ciphertext. \nA. Counter cipher mode \nB. Electronic Codebook cipher mode \nC. Cipher Block Chain\n'))
if question.lower() == 'c':
    print('Happy Ciphering!')
else: 
    print('Incorrect. Cipher Block Chaining uses XORed method with each block encryption')

question= str(input('7. Digital signatures allow us to send information to other parties and verify that the information wasnt changed. \nPlease select which method digital signatures do not provide. \nA. Confidentiality \nB. Integrity \nC. Non-repudiation \nD. Authentication\n'))
if question.lower() == 'a':
    print('Right On!')
    print('Thank you for playing my game, you\'re an encryption expert!\nHappy encrypting!')

else:
    print('Sorry. Digital Signatures prove several important: 1. Integrity - they ensure that nothing was changed in the message. , 2.Authentication - they verify the source of the message. , 3.Non-repudiation - they confirm the signature is genuine and not forged & 4. Verification - they demonstrate that the message was signed using both the public and private keys.')
    print('Thank you for playing my game, program complete!\nHappy encrypting!')
