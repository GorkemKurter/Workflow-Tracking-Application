from django.db import models

# Create your models here.
class Component(models.Model):
    
    parts = [("Main Motor - UM","Main Motor - UM"),("Main motor - BLDC","Main motor - BLDC"),("Drain pump (for twin jet system)",
             "Drain pump (for twin jet system)"),
             ("Drain pump","Drain pump"),("Circulation pump (for twin jet system)","Circulation pump (for twin jet system)"),
             ("Drain pump (twin jet system) (with emergency exit hose)","Drain pump (twin jet system) (with emergency exit hose)"),
             ("Dosage pump","Dosage pump"),
             ("Hydroboost pump","Hydroboost pump"),("Capacitor (for Hydro-boost pump)","Capacitor (for Hydro-boost pump)"),
             ("Thermal Protector","Thermal Protector"),("Belt (BLDC models)","Belt (BLDC models)"),
             ("Electrically operated door lock","Electrically operated door lock"),
             ("Door switch with interlock","Door switch with interlock"),
             ("Heating element","Heating element"),("with 2 fuse","with 2 fuse"),
             ("with alternative 2 fuse","with alternative 2 fuse"),("Heating element (Pyrojet)","Heating element (Pyrojet)"),
             ("Inlet valve (double)","Inlet valve (double)"),("Inlet valve (single)","Inlet valve (single)"),
             ("Inlet valve (triple)","Inlet valve (triple)"),("Level switch","Level switch"),
             ("Level sensor","Level sensor"),("NTC","NTC"),
             ("Reed Switch","Reed Switch"),("Steam Generator","Steam Generator"),("with Thermostat","with Thermostat"),
             ("Thermostat for Pyrojet Heating Element","Thermostat for Pyrojet Heating Element"),
             ("Overflow Switch","Overflow Switch"),("Electronic Module - BLDC Board","Electronic Module - BLDC Board"),
             ("Electronic Module - DC Board","Electronic Module - DC Board"),
             ("Electronic Module - Steamjet, Pyrojet, Dryer Board","Electronic Module - Steamjet, Pyrojet, Dryer Board"),
             ("Electronic Module - IO Board","Electronic Module - IO Board"),
             ("Electronic Module - Door Light Board","Electronic Module - Door Light Board"),
             ("Electronic Module - Main Board","Electronic Module - Main Board"),
             ("Electronic Module - UI Board","Electronic Module - UI Board"),("Drum Light Board","Drum Light Board"),
             ("Electronic Module - Sterilizone IO Board","Electronic Module - Sterilizone IO Board"),
             ("Electronic Module - Intelliwash IO Board","Electronic Module - Intelliwash IO Board"),
             ("Electronic Module - LED Board","Electronic Module - LED Board"),
             ("Electronic Module - UV Ballast Board","Electronic Module - UV Ballast Board"),
             ("Electronic Module - UV Lamp Board","Electronic Module - UV Lamp Board"),
             ("Electronic Module - Wifi Board","Electronic Module - Wifi Board"),("EMI filter","EMI filter"),
             ("Current Fuse","Current Fuse"),("Microcontroller - BLDC Board","Microcontroller - BLDC Board"),
             ("Microcontroller - Main Board","Microcontroller - Main Board"),("Optocoupler","Optocoupler"),
             ("Optotriac","Optotriac"),("Relay on PCB","Relay on PCB"),
             ("Safety Transformer","Safety Transformer"),("Switch on PCB","Switch on PCB"),
             ("Varistor","Varistor"),("XY Capacitor","XY Capacitor"),
             ("Plug Current Fuse","Plug Current Fuse"),("hose set (cold)","hose set (cold)"),
             ("hose set (hot)","hose set (hot)"),("Check Valve","Check Valve"),
             ("Supply cord","Supply cord"),("Plug","Plug"),("Electronic Module - Integrated Board","Electronic Module - Integrated Board")]
        
    Part_name = models.CharField(verbose_name="Object / part No.",max_length=100,choices=parts)
    Manufacturer = models.CharField(verbose_name="Manufacturer/ trademark",max_length=150)
    Model = models.CharField(verbose_name="Type/Model",max_length=120)
    Technical_Data = models.TextField(verbose_name="Technical Data")
    Standard = models.TextField(verbose_name="Standard(s)")
    Mark_of_Conformity = models.CharField(verbose_name="Mark(s) of Conformity",max_length=120)
    T_Washer_LVD = models.BooleanField(verbose_name="T washer",default=False)
    T_Washer_Dryer_LVD = models.BooleanField(verbose_name="T washer dryer",default=False)
    F_Washer_LVD = models.BooleanField(verbose_name="F washer",default=False)
    F_Washer_Dryer_LVD = models.BooleanField(verbose_name="F washer dryer",default=False)
    N_Washer_LVD = models.BooleanField(verbose_name="N washer",default=False)
    SAP_code = models.CharField(verbose_name="SAP Code",max_length=80)
    Certificate_Expiry_Date = models.DateField(verbose_name = 'Certificate Expiry Date')
    Test_Results_Link = models.CharField(verbose_name='Test Reports & Certificate Link',max_length=1000)
    Created_Date = models.DateField(auto_now_add=True,verbose_name='Created Date')
    Last_Update_Date = models.DateField(auto_now=True,verbose_name='Last Update')
    def __str__(self):
        return self.Model
    
class Component_Request(models.Model):
    R_parts = [("Main Motor - UM","Main Motor - UM"),("Main motor - BLDC","Main motor - BLDC"),("Drain pump (for twin jet system)",
             "Drain pump (for twin jet system)"),
             ("Drain pump","Drain pump"),("Circulation pump (for twin jet system)","Circulation pump (for twin jet system)"),
             ("Drain pump (twin jet system) (with emergency exit hose)","Drain pump (twin jet system) (with emergency exit hose)"),
             ("Dosage pump","Dosage pump"),
             ("Hydroboost pump","Hydroboost pump"),("Capacitor (for Hydro-boost pump)","Capacitor (for Hydro-boost pump)"),
             ("Thermal Protector","Thermal Protector"),("Belt (BLDC models)","Belt (BLDC models)"),
             ("Electrically operated door lock","Electrically operated door lock"),
             ("Door switch with interlock","Door switch with interlock"),
             ("Heating element","Heating element"),("with 2 fuse","with 2 fuse"),
             ("with alternative 2 fuse","with alternative 2 fuse"),("Heating element (Pyrojet)","Heating element (Pyrojet)"),
             ("Inlet valve (double)","Inlet valve (double)"),("Inlet valve (single)","Inlet valve (single)"),
             ("Inlet valve (triple)","Inlet valve (triple)"),("Level switch","Level switch"),
             ("Level sensor","Level sensor"),("NTC","NTC"),
             ("Reed Switch","Reed Switch"),("Steam Generator","Steam Generator"),("with Thermostat","with Thermostat"),
             ("Thermostat for Pyrojet Heating Element","Thermostat for Pyrojet Heating Element"),
             ("Overflow Switch","Overflow Switch"),("Electronic Module - BLDC Board","Electronic Module - BLDC Board"),
             ("Electronic Module - DC Board","Electronic Module - DC Board"),
             ("Electronic Module - Steamjet, Pyrojet, Dryer Board","Electronic Module - Steamjet, Pyrojet, Dryer Board"),
             ("Electronic Module - IO Board","Electronic Module - IO Board"),
             ("Electronic Module - Door Light Board","Electronic Module - Door Light Board"),
             ("Electronic Module - Main Board","Electronic Module - Main Board"),
             ("Electronic Module - UI Board","Electronic Module - UI Board"),("Drum Light Board","Drum Light Board"),
             ("Electronic Module - Sterilizone IO Board","Electronic Module - Sterilizone IO Board"),
             ("Electronic Module - Intelliwash IO Board","Electronic Module - Intelliwash IO Board"),
             ("Electronic Module - LED Board","Electronic Module - LED Board"),
             ("Electronic Module - UV Ballast Board","Electronic Module - UV Ballast Board"),
             ("Electronic Module - UV Lamp Board","Electronic Module - UV Lamp Board"),
             ("Electronic Module - Wifi Board","Electronic Module - Wifi Board"),("EMI filter","EMI filter"),
             ("Current Fuse","Current Fuse"),("Microcontroller - BLDC Board","Microcontroller - BLDC Board"),
             ("Microcontroller - Main Board","Microcontroller - Main Board"),("Optocoupler","Optocoupler"),
             ("Optotriac","Optotriac"),("Relay on PCB","Relay on PCB"),
             ("Safety Transformer","Safety Transformer"),("Switch on PCB","Switch on PCB"),
             ("Varistor","Varistor"),("XY Capacitor","XY Capacitor"),
             ("Plug Current Fuse","Plug Current Fuse"),("hose set (cold)","hose set (cold)"),
             ("hose set (hot)","hose set (hot)"),("Check Valve","Check Valve"),
             ("Supply cord","Supply cord"),("Plug","Plug"),("Electronic Module - Integrated Board","Electronic Module - Integrated Board")]
    R_Requester = models.ForeignKey("auth.User",on_delete = models.PROTECT,default = 1,verbose_name='Requester')
    R_Part_name = models.CharField(verbose_name="Object / part No.",max_length=100,choices=R_parts)
    R_Manufacturer = models.CharField(verbose_name="Manufacturer/ trademark",max_length=150)
    R_Model = models.CharField(verbose_name="Type/Model",max_length=120)
    R_Technical_Data = models.TextField(verbose_name="Technical Data")
    R_Determination = models.TextField(verbose_name="Explanation about usage of component")
    R_T_Washer_LVD = models.BooleanField(verbose_name="T washer",default=False)
    R_T_Washer_Dryer_LVD = models.BooleanField(verbose_name="T washer dryer",default=False)
    R_F_Washer_LVD = models.BooleanField(verbose_name="F washer",default=False)
    R_F_Washer_Dryer_LVD = models.BooleanField(verbose_name="F washer dryer",default=False)
    R_N_Washer_LVD = models.BooleanField(verbose_name="N washer",default=False)
    R_SAP_code = models.CharField(verbose_name="SAP Code",max_length=80)
    R_Status_Parts = [("Approved","Approved"),("Pending","Pending"),("Rejected","Rejected")]
    R_Status = models.CharField(verbose_name="Status",max_length=100,choices=R_Status_Parts, default = 'Pending')
    Pre_Series_Date = models.DateField(verbose_name = 'Date of Pre Series',help_text='Hint : Enter date in format YYYY-MM-DD')
    Test_Results_Link = models.CharField(verbose_name='Test Reports & Certificate Link',max_length=1000,
                                         help_text='Warning : Folder must be placed in the local network VBCARGE')
    R_Created_Date = models.DateField(auto_now_add=True,verbose_name='Created Date')
    R_Last_Update_Date = models.DateField(auto_now=True,verbose_name='Last Update')
    R_Priority_Choices = [("High","High"),("Normal","Normal"),("Low","Low")]
    R_Priority = models.CharField(verbose_name='Priority',choices=R_Priority_Choices,default='Normal',max_length=40)
    #R_Test_Results = models.FileField(upload_to='test_results/', verbose_name="Upload Test Results", null=True, blank=True)

    def __str__(self):
        return self.R_Model