print "........WELCOME TO RESULT PORTAL........."
import time
name={
   
  
   "Moshabbar": [
      "Name:MOSHABBAR HUSSAIN",
      "Roll No-::AS6789",
      "...........Moshabbar::Marksheet...............",
      
      "PHYSICS MARK----::78",
      "CHEMISTRY MARK--::90",
      "MATH MARK-------::78",
      "BIOLOGY MARK----::67",
      "ENGLISH MARK----::71",
      "HINDI MARK------::89",
      "...................................",
      "Total-----------::473",
      "Percentage::78.83%",
      "Result:Passed with First Class"
   ],
   

   "Rahul": [
      "Name:RAHUL AMEEN",
      "Roll No-::AS8780",
      "...........Rahul::Marksheet...............",
      
      "PHYSICS MARK-----::71",
      "CHEMISTRY MARK---::80",
      "MATH MARK--------::78",
      "BIOLOGY MARK-----::67",
      "ENGLISH MARK-----::71",
      "HINDI MARK-------::50",
      "...................................",
      "Total------------::417",
      "Percentage::69.5%",
      "Result:Passed with First Class"
   ],

   "Ashu": [
      "Name:ASHU JHARKAND",
      "Roll No--::AS9719",
      "...........Ashu::Marksheet...............",
      
      "PHYSICS MARK----::89",
      "CHEMISTRY MARK--::90",
      "MATH MARK-------::88",
      "BIOLOGY MARK----::77",
      "ENGLISH MARK----::71",
      "HINDI MARK------::99",
      "...................................",
      "Total-----------::514",
      "Percentage::85.66%",
      "Result:Passed with First Class with Distinction"
   ],
   
   "Ameer": [
      "Name:AMEER HUSSAIN" ,
      "Roll No--::AS2780",
      "...........Ameer::Marksheet...............",
      
      "PHYSICS MARK-----::89",
      "CHEMISTRY MARK---::90",
      "MATH MARK--------::88",
      "BIOLOGY MARK-----::77",
      "ENGLISH MARK-----::71",
      "HINDI MARK-------::99",
      "...................................",
      "Total------------::514",
      "Percentage::85.66%",
      "Result:Passed with First Class with Distinction"
   ],
   "Irshad": [
      "Name:IRSHAD SEIKH",
      "Roll No-::AS3781",
      "...........Irshad::Marksheet...............",
      
      "PHYSICS MARK------::79",
      "CHEMISTRY MARK----::55",
      "MATH MARK---------::67",
      "BIOLOGY MARK------::77",
      "ENGLISH MARK------::71",
      "HINDI MARK--------::67",
      "...................................",
      "Total-------------::416",
      "Percentage::69.33%",
      "Result:Passed with First Class"
   ],
   "Resmi": [
      "Name:RESMI KHATUN",
      "Roll No-::AS4780",
      "...........Resmi::Marksheet...............",
      
      "PHYSICS MARK------::35",
      "CHEMISTRY MARK----::40",
      "MATH MARK---------::38",
      "BIOLOGY MARK------::47",
      "ENGLISH MARK------::31",
      "HINDI MARK--------::59",
      "...................................",
      "Total-------------::250",
      "Percentage::41.66%",
      "Result:Passed with Third Class"
   ],
   "Haidar": [
      "Name:HAIDER ALI",
      "Roll No-::AS6181",
      "...........Haider::Marksheet...............",
      
      "PHYSICS MARK------::49",
      "CHEMISTRY MARK----::50",
      "MATH MARK---------::68",
      "BIOLOGY MARK------::37",
      "ENGLISH MARK------::51",
      "HINDI MARK--------::59",
      "...................................",
      "Total-------------::314",
      "Percentage::52.33%",
      "Result:Passed with Second Class"
   ]
    
}
## If you want to get data from database and want Result just connect with database and .....coding like below...
Roll_No=raw_input(str("Enter your Name:"))
if(Roll_No=="AS6789" or Roll_No=="AS8780" or Roll_No=="AS9719" or Roll_No=="AS2780"
   or Roll_No=="AS3781" or Roll_No=="AS4780" or Roll_No=="AS6181"):
    if(Roll_No=="AS6789"):
        #print name["Moshabbar"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Moshabbar"]:
            print result

    elif(Roll_No=="AS8780"):
        #print name["Rahul"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Rahul"]:
            print result

    elif(Roll_No=="AS9719"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Ashu"]:
            print result


    elif(Roll_No=="AS2780"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Ameer"]:
            print result

    elif(Roll_No=="AS3781"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Irshad"]:
            print result

    elif(Roll_No=="AS4780"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Haider"]:
            print result
            
    elif(Roll_No=="AS6181"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Resmi"]:
            print result        
            

            
else:
    print "You Entered Correct Roll No it is not Matching"
