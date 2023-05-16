import requests
import hashlib
import sys

#requesting for API data
def request_api_data(query_character):
  url = 'https://api.pwnedpasswords.com/range/' + query_character
  response = requests.get(url)
  if response.status_code != 200:
    raise RuntimeError(f'Error Fetching: {response.status_code} check the API and try again ')
  return response

#matching my hash code with the list
def get_password_leaks_count(hashes , hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0  

#checking how many times password has pwned and converting string into sha1 hash code
def pwned_api_check(password):
  #converting string into sha1 hash code
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  #grabing first 5 and rest values of our sha1 hash code
  first5_characters ,rest_characters  = sha1password[:5] , sha1password[5:]
  response2 = request_api_data(first5_characters)
  print(response2)
  return get_password_leaks_count(response2, rest_characters)

#simply setting the function for showing output
def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times...You should probably change it!')
    else:
      print(f'{password} was not found. Carry on!')
  return 'Your password has checked safely!'    


#for top security reasons taking txt/word/pdf files as input
input_file = sys.argv[1] 
with open(f'{input_file}', mode ='r') as mypassword:
  content = mypassword.readlines()


if __name__ == '__main__':
  sys.exit(main(content))
  



