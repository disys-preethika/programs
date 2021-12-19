def BankingSBIstatement():
    BankName="SBIBank"
    Date="29/05/14"
    Time="19:48"
    ATMNo="SJNBL48"
    CARDNo="xxxxxxxxxxxxx0516"
    BRANCHNAME="Bangalore Main Branch"
    TxnNo=2907
    Responsecode="072"
    WithDrawl="500.00"
    account="xxxxxxxxxx05xx01"
    ModRS="0.00"
    AvailableBalRs="1000.00"
    Website="www.statebankofindia.com"
    print(BankName,BRANCHNAME)
    return
BankingSBIstatement()

    

def CreatingGoogleAccount():


    FirstName="venkatesh"
    LastName="db"
    ChooseUsername="jvt"
    CreataPassword="balu"
    ConfirmYourPassword="balu"
    Birthday="2-6-1986"
    Gender="male"
    Mobile=9900367097
    Yourcurrentemailaddress="venkatesh.db@gmail.com"
    print(FirstName,LastName,Birthday,Mobile,Yourcurrentemailaddress)
    return
CreatingGoogleAccount()

def Outstanding():

    Total="Rs.571.36"
    Unbilled="Rs.0"
    LastPaymentMadeAmount="Rs.0"
    Date="10/1/2020"
    CreditLimitTotal="Rs.18,000"
    Available="Rs.17,428.64"
    Utilization="3%"
    CashLimitTotal="Rs.3,600"
    Available1="Rs.3,600"
    print(Total,CreditLimitTotal,Available,CashLimitTotal)
    return

Outstanding()

def SystemProperties():
    Rating="4.5"
    Processor="Intel®Core™i5-2450CPU"
    RAM="4.00GB"
    SystemType="64-bitOperating System"
    PenandTouch="NoPenorTouchInputisavailableforthisDisplay" 
    ComputerName="BALU-PC"
    ComputerDescription="WORKGROUP"
    WindowsEdition="Windows7Ultimate"
    WindowsProductID="00426-OEM-8992662-00497"
    print(Rating,Processor,InstalledMemory(RAM),InstalledMemory(RAM),ComputerName)
    return

def Vehicle():
    car="lightmotorvehicle-car"
    Colour="red"
    Enginenumber="kp98gtyihh457797"
    Chassisnumber="tc5678898335r45"
    Company="BMW"
    print(Colour,car,Enginenumber,Chassisnumber,Company)
    return
Vehicle()




def visitingcarddetails():
    name="naresh"
    mailid="naresh00@gmail.com"
    contactno="+919944860792"
    companyname="jvt"
    designation="programmer"
    address="230/32ndfloorhal3rdstagenewthippasandrabangalore-560075"
    print(name,mailid,contactno,companyname,designation)
    return
visitingcarddetails()

class basicinformation:
    Name="JVT"
    Age=5
    Gender="Male"
    EmailAddress="info@jvtechnologies.co.in"
    PhotoIDCard="VoterIdorRation card"
    IDCardNo="ASUPB590F"
    Name="Mr.venkatesh"
    Age=25
    Gender="Male"
    EmailAddress="venkatesh.db@gmail.com"
    Address="BEMLMainRoad"
    City="Bangalore"
    State="Karnataka"
    JVTPincode="560075"
    Country="India"
    MobileNo="9900367097"
    PhotoID="Passport"
    PhotoIDNo="G3839975"

JVT=basicinformation()
print(JVT.Name,JVT.Age,JVT.PhotoIDCard,JVT.EmailAddress,JVT.MobileNo,JVT.PhotoIDNo)


def visitingcarddetails(name,mailid,contactno,companyname,designation,address):
    print(name,mailid,contactno,companyname,designation,address)
    return
visitingcarddetails("naresh","naresh00@gmail.com","+919944860792","jvt","programmer","230/32ndfloorhal3rdstagenewthippasandrabangalore-560075")



allpt=["pt1","pt2"]

def hc(patientname,patientid):
    if(patientid in allpt):
        print(patientname,patientid)
    else:
        print("notvalid id")

    return 0


ret=hc("mani","pt1")

hc("abi","pt13")



def ticket():

        TicketType="SpecialEntryDarshan"
        Date="Dec1st"
        Day="Tuesday"
        Time="3:30Am" 
        PerSlotTickets="2000"
        BookingNo="IS151110080016"
        NameofthePilgrim="venkatesh"
        OrderNo="010600013554"
        Email="venkateshprofessional7@gmail.com"
        AmountinfiguresRs="220.00"
        AadhaarCard="733498928758"
        BookedDateandTime="1106201511:36:46"
        NoofPersons=1
        NameoftheSevaDarshan="Archana"
        ReportingTime="4:00AM"
        PerformanceDateandTime="12012015AM4:30:00"
        PrivilegestotheSeva="TwoSmallLaddu"
        BookedTime="11:36:46"
        AccommodationType="Rs500Tirumala"
        Available=350
        NoofTickets=1
        Rate="50to2000"
        print(TicketType,PerSlotTickets,BookingNo,NameofthePilgrim,OrderNo,AadhaarCard,BookedTime,NoofTickets)
        return


ticket()


def Electricbillpaidvianetbanking():


    website="www.tnebnet.org"
    tnebusername="agilan"
    password="1234567"
    consumernumber=23456123
    Billingstatus="paidorunpaid"
    modeofpayment="netbanking"
    choosebank="sbi"
    username="kumar007"
    password=1234567
    Transactionno="18cv21828578437"
    paymentstatus="successful"

    print(website,tnebusername,consumernumber,Billingstatus,username,paymentstatus)

    return


Electricbillpaidvianetbanking()

class Scott:

        Brand        ="ScottInternational"
        ProductCode ="APPSCOTT-INTERNSWIT610835D77A441"
        Color        ="Black"
        Size         ="S"
        Material     ="Cotton" 
        Occasion     ="Casual"
        Pattern      ="Solid"
        Sleeve       ="FullSleeves"
        NeckType    ="Hooded"
        Fit          ="Slim"
        Gender       ="Men"

class SHIPPINGDETAILS(Scott):


        EstimatedArrival ="9days"

        ReturnPolicy     ="Sellerwillacceptreturnswithina15daysfromdateofdeliveryoftheitem"

        BuyforRS =824

        EffectivePrice="Rs453aftercashback"

        
Sellerwillacceptreturnswithina15daysfromdateofdeliveryoftheitem=SHIPPINGDETAILS(Scott)

print(Sellerwillacceptreturnswithina15daysfromdateofdeliveryoftheitem.EstimatedArrival,Sellerwillacceptreturnswithina15daysfromdateofdeliveryoftheitem.Brand )



