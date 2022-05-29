library(dplyr)
library(tidyr)
library(jsonlite)
library(httr)
library(stringr)
library(ggplot2)


print("when you guess a word use lower case")
print("when you input results, use upper case")
print("Guess: cares")
test = five.word
guess = "cares"
str <- c()
Y = "Y"
result = ""

while(result != "YES") {
  result = readline(prompt="Correct? (YES / NO):")
  
  if(result == "YES") {
    print("nice")
    break
  }
  
  if(result == "NO") {
    print("G for green")
    print("N for grey")
    print("Y for yellow")
    print("input these characters in order")
    color = readline(prompt = "Enter results: ")
  }
  
  poop = data.frame('ans' = as.character(color))
  ################################################### first letter
  if(substring(poop[,1], 1, 1) == "G") {
    test <- location_conf(test, substring(pee,1,1),1)
  } 
  
  if(substring(poop[,1], 1, 1) == "N") {
    test <- word_remover(test, substring(pee,1,1))
  } 
  
  if(substring(poop[,1], 1, 1) == "Y") {
    test <- location_remover(test, substring(pee,1,1),1)
    str <- append(str, substring(pee,1,1))
  } 
  ################################################### second letter 
  if(substring(poop[,1], 2, 2) == "G") {
    test <- location_conf(test, substring(pee,2,2),2)
  } 
  
  if(substring(poop[,1], 2, 2) == "N") {
    test <- word_remover(test, substring(pee,2,2))
  } 
  
  if(substring(poop[,1], 2, 2) == "Y") {
    test <- location_remover(test, substring(pee,2,2),2)
    str <- append(str, substring(pee,2,2))
  } 
  ################################################### third letter 
  if(substring(poop[,1], 3, 3) == "G") {
    test <- location_conf(test, substring(pee,3,3),3)
  } 
  
  if(substring(poop[,1], 3, 3) == "N") {
    test <- word_remover(test, substring(pee,3,3))
  } 
  
  if(substring(poop[,1], 3, 3) == "Y") {
    test <- location_remover(test, substring(pee,3,3),3)
    str <- append(str, substring(pee,3,3))
  } 
  ################################################### fourth letter 
  if(substring(poop[,1], 4, 4) == "G") {
    test <- location_conf(test, substring(pee,4,4),4)
  } 
  
  if(substring(poop[,1], 4, 4) == "N") {
    test <- word_remover(test, substring(pee,4,4))
  } 
  
  if(substring(poop[,1], 4, 4) == "Y") {
    test <- location_remover(test, substring(pee,4,4),4)
    str <- append(str, substring(pee,4,4))
  } 
  ################################################### fifth letter 
  if(substring(poop[,1], 5, 5) == "G") {
    test <- location_conf(test, substring(pee,5,5),5)
  } 
  
  if(substring(poop[,1], 5, 5) == "N") {
    test <- word_remover(test, substring(pee,5,5))
  } 
  
  if(substring(poop[,1], 5, 5) == "Y") {
    test <- location_remover(test, substring(pee,5,5),5)
    str <- append(str, substring(pee,5,5))
  } 
  #######
  
  if(grepl(poop, Y) == TRUE) {
    test2 <- test$test #first subset
    
    plz <- data.frame(sapply(str, grepl, test2))  #shows which ones are false
    
    plz$word <- test2
    
    plz[(plz == "FALSE")] <- NA
    
    plz <- na.omit(plz)
    
    test <- plz[,(length(plz)), drop = FALSE] #this will be the final return 
  } 
  #######
  
  guess <- guesser(test, alp)
  
  print("guess this word:")
  print(guess)
  pee = guess
  
}