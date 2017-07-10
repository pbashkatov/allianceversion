# allianceversion
Get SWIFTAlliance software version and patches installed 

SNL command 'swiftnet version -a' showing SNL and SAG version, patches, COTS packages. Unfortunately there are no similar commands for SAA/SAE/SWP. 

This simple script collects the version and owner information for Alliance software. The report looks like this:  

=====     Found installed SWIFTAlliance products     =====

SWIFTNet Link                            : C:\SWIFT\SNL
SWIFTAlliance Gateway                    : C:\Alliance\Gateway
SWIFTAlliance Access                     : C:\Alliance\Access
SWIFTAlliance WebPlatform                : C:\Alliance\SWPSE

=====     SWIFTNet Link     =====

for SNL version info use 'swiftnet version -a' command from SNL command line
this command must be run under the SNL owner credentials

=====     SWIFTAlliance Gateway     =====

Gateway Owner Name               : all_adm
Gateway Owner Credentials        : VMSWIFTPROD\\all_adm
Gateway Base Version             : 7.0.50.11

=====     SWIFTAlliance Access     =====

Access Owner Name                : Administrator
Access Owner Credentials         : AH02\\Administrator
Access Base Version              : 7.1.0.76
Access Delta Base Version        : 7.1.0
Access Delta Patch Version       : 7.1.10

Number of patches installed: 4
(1) build number : 7.1.10.15    version : 7.1.10
(2) build number : 7.1.20.22    version : 7.1.20
(3) build number : 7.1.23.3     version : 7.1.23
(4) build number : 7.1.30.5     version : 7.1.30

Number of security updates installed : 2
(1) update version : ogs.15
(2) update version : 201705

=====     SWIFTAlliance WebPlatform     =====

WebPlatform Owner Name           : Administrator
WebPlatform Owner Credentials    : AH02\\Administrator
WebPlatform Base Version         : 7.0.70.4

Number of security updates installed : 2
(1) update version : ogs.16
(2) update version : 201705
# ---------------------------------------------------------------------- 
