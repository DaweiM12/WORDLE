#wordle test 

#logic of entering information 
my.name <- readline(prompt="Enter name: ")
my.age <- readline(prompt="Enter age: ")
# convert character into integer
my.age <- as.integer(my.age)
print(paste("Hi,", my.name, "next year you will be", my.age+1, "years old."))

#first pos
substring(poop[,1], 1, 1) == "G"
substring(poop[,1], 1, 1) == "N"
substring(poop[,1], 1, 1) == "Y"

#second pos
substring(poop[,1], 2, 2) == "G"
substring(poop[,1], 2, 2) == "N"
substring(poop[,1], 2, 2) == "Y"

#third pos
substring(poop[,1], 3, 3) == "G"
substring(poop[,1], 3, 3) == "N"
substring(poop[,1], 3, 3) == "Y"

#fourth pos
substring(poop[,1], 4, 4) == "G"
substring(poop[,1], 4, 4) == "N"
substring(poop[,1], 4, 4) == "Y"

#fifth pos 
substring(poop[,1], 5, 5) == "G"
substring(poop[,1], 5, 5) == "N"
substring(poop[,1], 5, 5) == "Y"


pee = "cares"

substring(pee,2,2) == "a"

test <- word_remover(test, substring(pee,1,1))




if(substring(poop[,1], 3, 3) == "G") {
  test <- location_conf(test, substring(pee,3,3),3)
} else {
  next
}

if(substring(poop[,1], 3, 3) == "N") {
  test <- word_remover(test, substring(pee,3,3))
} else {
  next
}

if(substring(poop[,1], 3, 3) == "Y") {
  test <- location_remover(test, substring(pee,3,3),3)
} else {
  next
}

str <- c()
str <- append(str, substring(pee,3,3))

str <- append(str, substring(pee,4,4))


Y = "Y"

if(grepl(poop, Y) == TRUE) {
  test2 <- test$test #first subset
  
  plz <- data.frame(sapply(str, grepl, test2))  #shows which ones are false
  
  plz$word <- test2
  
  plz[(plz == "FALSE")] <- NA
  
  plz <- na.omit(plz)
  
  test <- plz[,(length(plz)), drop = FALSE] #this will be the final return 
} 



guesser <- function(test, alp) {
  
  
  loc1 <- data.frame("letter" = sapply(alp,location_counter_1))
  loc1$percentage <- (loc1[,1]/ nrow(test))*100
  loc1$alp <- alp
  
  loc1[which.max(loc1[,2]),]
  
  loc2 <- data.frame("letter" = sapply(alp,location_counter_2))
  loc2$percentage <- (loc2[,1]/ nrow(test))*100
  loc2$alp <- alp
  
  loc2[which.max(loc2[,2]),]
  
  loc3 <- data.frame("letter" = sapply(alp,location_counter_3))
  loc3$percentage <- (loc3[,1]/ nrow(test))*100
  loc3$alp <- alp
  
  loc3[which.max(loc3[,2]),]
  
  loc4 <- data.frame("letter" = sapply(alp,location_counter_4))
  loc4$percentage <- (loc4[,1]/ nrow(test))*100
  loc4$alp <- alp
  
  loc4[which.max(loc4[,2]),]
  
  
  loc5 <- data.frame("letter" = sapply(alp,location_counter_5))
  loc5$percentage <- (loc5[,1]/ nrow(test))*100
  loc5$alp <- alp
  
  loc5[which.max(loc5[,2]),]
  
  
  
  test$chance <- ""
  
  for(i in 1:nrow(test)) {
    
    temp1 <- substring(test[i,1],1,1)
    per1 <- loc1[loc1[,3] %in% temp1,2]
    temp2 <- substring(test[i,1],2,2)
    per2 <- loc2[loc2[,3] %in% temp2,2]
    temp3 <- substring(test[i,1],3,3)
    per3 <- loc3[loc3[,3] %in% temp3,2]
    temp4 <- substring(test[i,1],4,4)
    per4 <- loc4[loc4[,3] %in% temp4,2]
    temp5 <- substring(test[i,1],5,5)
    per5 <- loc5[loc5[,3] %in% temp5,2]
    
    test[i,2] <- (per1*per2*per3*per4*per5)
    
    
    
  }
  guess <- test[which.max(test[,2]),1]
  
  return(guess)
  
}


guess <- guesser(test, alp)

print(guess)

#second word here:

test = five.word

#cares 
test <- word_remover(test, "c")
test <- word_remover(test, "e")
test <- word_remover(test, "s")
test <- location_remover(test, "a",2)
test <- location_remover(test, "r",3)
#grain 
test <- word_remover(test, "g")
test <- word_remover(test, "n")
test <- location_conf(test, "a", 3)
test <- location_conf(test, "i", 4)
test <- location_remover(test, "r", 2)
#flair- correct 
