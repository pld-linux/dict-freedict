%define      dictname    freedict
%define      dict1    afr-deu
%define      dict2    cze-eng
%define      dict3    dan-eng
%define      dict4    deu-eng
%define      dict5    deu-fra
%define      dict6    deu-ita
%define      dict7    deu-nld
%define      dict8    deu-por
%define      dict9    eng-deu
%define      dict10    eng-fra
%define      dict11    eng-hun
%define      dict12    eng-iri
#%define      dict13    eng-ita
%define      dict14    eng-lat
%define      dict15    eng-nld
%define      dict16    eng-por
%define      dict17    eng-rus
%define      dict18    eng-scr
%define      dict19    eng-spa
%define      dict20    eng-swe
%define      dict21    eng-wel
%define      dict22    fra-deu
%define      dict23    fra-eng
%define      dict24    fra-nld
%define      dict25    gre-deu
%define      dict26    hun-eng
%define      dict27    iri-eng
%define      dict28    ita-deu
%define      dict29    ita-eng
%define      dict30    jpn-deu
%define      dict31    lat-deu
%define      dict32    lat-eng
%define      dict33    nld-deu
%define      dict34    nld-eng
%define      dict35    nld-fra
%define      dict36    por-deu
%define      dict37    por-eng
%define      dict38    sco-deu
%define      dict39    scr-eng
%define      dict40    slo-eng
%define      dict41    spa-eng
%define      dict42    swa-eng
%define      dict43    swe-eng
%define      dict44    tur-deu
%define      dict45    tur-eng
%define      dict46    wel-eng
# removed dict25 dict29 --undefine's patch.
%define      dictionaries %{dict1} %{dict2} %{dict3} %{dict4} %{dict5} %{dict6} %{dict7} %{dict8} %{dict9} %{dict10} %{dict11} %{dict12} %{dict14} %{dict15} %{dict16} %{dict17} %{dict18} %{dict19} %{dict20} %{dict21} %{dict22} %{dict23} %{dict24} %{dict26} %{dict27} %{dict28} %{dict30} %{dict31} %{dict32} %{dict33} %{dict34} %{dict35} %{dict36} %{dict37} %{dict38} %{dict39} %{dict40} %{dict41} %{dict42} %{dict43} %{dict44} %{dict45} %{dict46}
# and no dict13, as says old custom

Summary:	The Free bilingual dictionaries for dictd
Summary(pl):	Darmowe dwuj瞛ykowe S這wniki dla dictd
Name:		%{dictname}
Version:	20020622
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://www.freedict.de/download/linux/dictmisc.tar.gz
Source1:    http://freedict.sourceforge.net/download/linux/%{dict1}.tar.gz
Source2:    http://freedict.sourceforge.net/download/linux/%{dict2}.tar.gz
Source3:    http://freedict.sourceforge.net/download/linux/%{dict3}.tar.gz
Source4:    http://freedict.sourceforge.net/download/linux/%{dict4}.tar.gz
Source5:    http://freedict.sourceforge.net/download/linux/%{dict5}.tar.gz
Source6:    http://freedict.sourceforge.net/download/linux/%{dict6}.tar.gz
Source7:    http://freedict.sourceforge.net/download/linux/%{dict7}.tar.gz
Source8:    http://freedict.sourceforge.net/download/linux/%{dict8}.tar.gz
Source9:    http://freedict.sourceforge.net/download/linux/%{dict9}.tar.gz
Source10:    http://freedict.sourceforge.net/download/linux/%{dict10}.tar.gz
Source11:    http://freedict.sourceforge.net/download/linux/%{dict11}.tar.gz
Source12:    http://freedict.sourceforge.net/download/linux/%{dict12}.tar.gz
#Source13:    http://freedict.sourceforge.net/download/linux/%{dict13}.tar.gz
Source14:    http://freedict.sourceforge.net/download/linux/%{dict14}.tar.gz
Source15:    http://freedict.sourceforge.net/download/linux/%{dict15}.tar.gz
Source16:    http://freedict.sourceforge.net/download/linux/%{dict16}.tar.gz
Source17:    http://freedict.sourceforge.net/download/linux/%{dict17}.tar.gz
Source18:    http://freedict.sourceforge.net/download/linux/%{dict18}.tar.gz
Source19:    http://freedict.sourceforge.net/download/linux/%{dict19}.tar.gz
Source20:    http://freedict.sourceforge.net/download/linux/%{dict20}.tar.gz
Source21:    http://freedict.sourceforge.net/download/linux/%{dict21}.tar.gz
Source22:    http://freedict.sourceforge.net/download/linux/%{dict22}.tar.gz
Source23:    http://freedict.sourceforge.net/download/linux/%{dict23}.tar.gz
Source24:    http://freedict.sourceforge.net/download/linux/%{dict24}.tar.gz
Source25:    http://freedict.sourceforge.net/download/linux/%{dict25}.tar.gz
Source26:    http://freedict.sourceforge.net/download/linux/%{dict26}.tar.gz
Source27:    http://freedict.sourceforge.net/download/linux/%{dict27}.tar.gz
Source28:    http://freedict.sourceforge.net/download/linux/%{dict28}.tar.gz
Source29:    http://freedict.sourceforge.net/download/linux/%{dict29}.tar.gz
Source30:    http://freedict.sourceforge.net/download/linux/%{dict30}.tar.gz
Source31:    http://freedict.sourceforge.net/download/linux/%{dict31}.tar.gz
Source32:    http://freedict.sourceforge.net/download/linux/%{dict32}.tar.gz
Source33:    http://freedict.sourceforge.net/download/linux/%{dict33}.tar.gz
Source34:    http://freedict.sourceforge.net/download/linux/%{dict34}.tar.gz
Source35:    http://freedict.sourceforge.net/download/linux/%{dict35}.tar.gz
Source36:    http://freedict.sourceforge.net/download/linux/%{dict36}.tar.gz
Source37:    http://freedict.sourceforge.net/download/linux/%{dict37}.tar.gz
Source38:    http://freedict.sourceforge.net/download/linux/%{dict38}.tar.gz
Source39:    http://freedict.sourceforge.net/download/linux/%{dict39}.tar.gz
Source40:    http://freedict.sourceforge.net/download/linux/%{dict40}.tar.gz
Source41:    http://freedict.sourceforge.net/download/linux/%{dict41}.tar.gz
Source42:    http://freedict.sourceforge.net/download/linux/%{dict42}.tar.gz
Source43:    http://freedict.sourceforge.net/download/linux/%{dict43}.tar.gz
Source44:    http://freedict.sourceforge.net/download/linux/%{dict44}.tar.gz
Source45:    http://freedict.sourceforge.net/download/linux/%{dict45}.tar.gz
Source46:    http://freedict.sourceforge.net/download/linux/%{dict46}.tar.gz
URL:		http://www.freedict.de
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	dictzip
BuildRequires:	autoconf
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description 
This package contains The The Free bilingual dictionaries, version %version
formatted for use by the dictionary server in the dictd package.

%description -l pl
Ten pakiet zawiera darmowe dwuj瞛yczne s這wniki w wersji %version
sformatowane do u篡tku z serwerem s這wnika dictd.

%package -n %{dictname}-%{dict1}
Summary:    The %{dict1} Dictionary for dictd
Summary(pl):    S這wnik %{dict1} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd 
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict1}
This package contains %{dict1} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict1}  -l pl
Ten pakiet zawiera s這wnik %{dict1} do u篡wania z serwerem s這wnika
dictd. 

%package -n %{dictname}-%{dict2}
Summary:    The %{dict2} Dictionary for dictd
Summary(pl):    S這wnik %{dict2} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict2}
This package contains %{dict2} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict2}  -l pl
Ten pakiet zawiera s這wnik %{dict2} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict3}
Summary:    The %{dict3} Dictionary for dictd
Summary(pl):    S這wnik %{dict3} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict3}
This package contains %{dict3} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict3}  -l pl
Ten pakiet zawiera s這wnik %{dict3} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict4}
Summary:    The %{dict4} Dictionary for dictd
Summary(pl):    S這wnik %{dict4} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict4}
This package contains %{dict4} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict4}  -l pl
Ten pakiet zawiera s這wnik %{dict4} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict5}
Summary:    The %{dict5} Dictionary for dictd
Summary(pl):    S這wnik %{dict5} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict5}
This package contains %{dict5} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict5}  -l pl
Ten pakiet zawiera s這wnik %{dict5} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict6}
Summary:    The %{dict6} Dictionary for dictd
Summary(pl):    S這wnik %{dict6} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict6}
This package contains %{dict6} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict6}  -l pl
Ten pakiet zawiera s這wnik %{dict6} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict7}
Summary:    The %{dict7} Dictionary for dictd
Summary(pl):    S這wnik %{dict7} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict7}
This package contains %{dict7} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict7}  -l pl
Ten pakiet zawiera s這wnik %{dict7} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict8}
Summary:    The %{dict8} Dictionary for dictd
Summary(pl):    S這wnik %{dict8} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict8}
This package contains %{dict8} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict8}  -l pl
Ten pakiet zawiera s這wnik %{dict8} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict9}
Summary:    The %{dict9} Dictionary for dictd
Summary(pl):    S這wnik %{dict9} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict9}
This package contains %{dict9} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict9}  -l pl
Ten pakiet zawiera s這wnik %{dict9} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict10}
Summary:    The %{dict10} Dictionary for dictd
Summary(pl):    S這wnik %{dict10} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict10}
This package contains %{dict10} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict10}  -l pl
Ten pakiet zawiera s這wnik %{dict10} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict11}
Summary:    The %{dict11} Dictionary for dictd
Summary(pl):    S這wnik %{dict11} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict11}
This package contains %{dict11} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict11}  -l pl
Ten pakiet zawiera s這wnik %{dict11} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict12}
Summary:    The %{dict12} Dictionary for dictd
Summary(pl):    S這wnik %{dict12} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict12}
This package contains %{dict12} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict12}  -l pl
Ten pakiet zawiera s這wnik %{dict12} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict13}
Summary:    The %{dict13} Dictionary for dictd
Summary(pl):    S這wnik %{dict13} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict13}
This package contains %{dict13} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict13}  -l pl
Ten pakiet zawiera s這wnik %{dict13} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict14}
Summary:    The %{dict14} Dictionary for dictd
Summary(pl):    S這wnik %{dict14} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict14}
This package contains %{dict14} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict14}  -l pl
Ten pakiet zawiera s這wnik %{dict14} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict15}
Summary:    The %{dict15} Dictionary for dictd
Summary(pl):    S這wnik %{dict15} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict15}
This package contains %{dict15} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict15}  -l pl
Ten pakiet zawiera s這wnik %{dict15} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict16}
Summary:    The %{dict16} Dictionary for dictd
Summary(pl):    S這wnik %{dict16} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict16}
This package contains %{dict16} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict16}  -l pl
Ten pakiet zawiera s這wnik %{dict16} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict17}
Summary:    The %{dict17} Dictionary for dictd
Summary(pl):    S這wnik %{dict17} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict17}
This package contains %{dict17} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict17}  -l pl
Ten pakiet zawiera s這wnik %{dict17} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict18}
Summary:    The %{dict18} Dictionary for dictd
Summary(pl):    S這wnik %{dict18} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict18}
This package contains %{dict18} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict18}  -l pl
Ten pakiet zawiera s這wnik %{dict18} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict19}
Summary:    The %{dict19} Dictionary for dictd
Summary(pl):    S這wnik %{dict19} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict19}
This package contains %{dict19} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict19}  -l pl
Ten pakiet zawiera s這wnik %{dict19} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict20}
Summary:    The %{dict20} Dictionary for dictd
Summary(pl):    S這wnik %{dict20} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict20}
This package contains %{dict20} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict20}  -l pl
Ten pakiet zawiera s這wnik %{dict20} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict21}
Summary:    The %{dict21} Dictionary for dictd
Summary(pl):    S這wnik %{dict21} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict21}
This package contains %{dict21} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict21}  -l pl
Ten pakiet zawiera s這wnik %{dict21} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict22}
Summary:    The %{dict22} Dictionary for dictd
Summary(pl):    S這wnik %{dict22} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict22}
This package contains %{dict22} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict22}  -l pl
Ten pakiet zawiera s這wnik %{dict22} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict23}
Summary:    The %{dict23} Dictionary for dictd
Summary(pl):    S這wnik %{dict23} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict23}
This package contains %{dict23} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict23}  -l pl
Ten pakiet zawiera s這wnik %{dict23} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict24}
Summary:    The %{dict24} Dictionary for dictd
Summary(pl):    S這wnik %{dict24} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict24}
This package contains %{dict24} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict24}  -l pl
Ten pakiet zawiera s這wnik %{dict24} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict25}
Summary:    The %{dict25} Dictionary for dictd
Summary(pl):    S這wnik %{dict25} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict25}
This package contains %{dict25} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict25}  -l pl
Ten pakiet zawiera s這wnik %{dict25} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict26}
Summary:    The %{dict26} Dictionary for dictd
Summary(pl):    S這wnik %{dict26} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict26}
This package contains %{dict26} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict26}  -l pl
Ten pakiet zawiera s這wnik %{dict26} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict27}
Summary:    The %{dict27} Dictionary for dictd
Summary(pl):    S這wnik %{dict27} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict27}
This package contains %{dict27} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict27}  -l pl
Ten pakiet zawiera s這wnik %{dict27} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict28}
Summary:    The %{dict28} Dictionary for dictd
Summary(pl):    S這wnik %{dict28} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict28}
This package contains %{dict28} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict28}  -l pl
Ten pakiet zawiera s這wnik %{dict28} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict29}
Summary:    The %{dict29} Dictionary for dictd
Summary(pl):    S這wnik %{dict29} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict29}
This package contains %{dict29} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict29}  -l pl
Ten pakiet zawiera s這wnik %{dict29} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict30}
Summary:    The %{dict30} Dictionary for dictd
Summary(pl):    S這wnik %{dict30} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict30}
This package contains %{dict30} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict30}  -l pl
Ten pakiet zawiera s這wnik %{dict30} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict31}
Summary:    The %{dict31} Dictionary for dictd
Summary(pl):    S這wnik %{dict31} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict31}
This package contains %{dict31} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict31}  -l pl
Ten pakiet zawiera s這wnik %{dict31} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict32}
Summary:    The %{dict32} Dictionary for dictd
Summary(pl):    S這wnik %{dict32} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict32}
This package contains %{dict32} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict32}  -l pl
Ten pakiet zawiera s這wnik %{dict32} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict33}
Summary:    The %{dict33} Dictionary for dictd
Summary(pl):    S這wnik %{dict33} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict33}
This package contains %{dict33} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict33}  -l pl
Ten pakiet zawiera s這wnik %{dict33} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict34}
Summary:    The %{dict34} Dictionary for dictd
Summary(pl):    S這wnik %{dict34} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict34}
This package contains %{dict34} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict34}  -l pl
Ten pakiet zawiera s這wnik %{dict34} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict35}
Summary:    The %{dict35} Dictionary for dictd
Summary(pl):    S這wnik %{dict35} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict35}
This package contains %{dict35} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict35}  -l pl
Ten pakiet zawiera s這wnik %{dict35} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict36}
Summary:    The %{dict36} Dictionary for dictd
Summary(pl):    S這wnik %{dict36} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict36}
This package contains %{dict36} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict36}  -l pl
Ten pakiet zawiera s這wnik %{dict36} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict37}
Summary:    The %{dict37} Dictionary for dictd
Summary(pl):    S這wnik %{dict37} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict37}
This package contains %{dict37} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict37}  -l pl
Ten pakiet zawiera s這wnik %{dict37} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict38}
Summary:    The %{dict38} Dictionary for dictd
Summary(pl):    S這wnik %{dict38} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict38}
This package contains %{dict38} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict38}  -l pl
Ten pakiet zawiera s這wnik %{dict38} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict39}
Summary:    The %{dict39} Dictionary for dictd
Summary(pl):    S這wnik %{dict39} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict39}
This package contains %{dict39} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict39}  -l pl
Ten pakiet zawiera s這wnik %{dict39} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict40}
Summary:    The %{dict40} Dictionary for dictd
Summary(pl):    S這wnik %{dict40} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict40}
This package contains %{dict40} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict40}  -l pl
Ten pakiet zawiera s這wnik %{dict40} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict41}
Summary:    The %{dict41} Dictionary for dictd
Summary(pl):    S這wnik %{dict41} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict41}
This package contains %{dict41} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict41}  -l pl
Ten pakiet zawiera s這wnik %{dict41} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict42}
Summary:    The %{dict42} Dictionary for dictd
Summary(pl):    S這wnik %{dict42} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict42}
This package contains %{dict42} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict42}  -l pl
Ten pakiet zawiera s這wnik %{dict42} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict43}
Summary:    The %{dict43} Dictionary for dictd
Summary(pl):    S這wnik %{dict43} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict43}
This package contains %{dict43} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict43}  -l pl
Ten pakiet zawiera s這wnik %{dict43} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict44}
Summary:    The %{dict44} Dictionary for dictd
Summary(pl):    S這wnik %{dict44} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict44}
This package contains %{dict44} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict44}  -l pl
Ten pakiet zawiera s這wnik %{dict44} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict45}
Summary:    The %{dict45} Dictionary for dictd
Summary(pl):    S這wnik %{dict45} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict45}
This package contains %{dict45} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict45}  -l pl
Ten pakiet zawiera s這wnik %{dict45} do u篡wania z serwerem s這wnika
dictd.

%package -n %{dictname}-%{dict46}
Summary:    The %{dict46} Dictionary for dictd
Summary(pl):    S這wnik %{dict46} dla dictd
Group:      Applications/Dictionaries
Requires:   dictd
Requires:   %{_sysconfdir}/dictd

%description -n  %{dictname}-%{dict46}
This package contains %{dict46} dictionaries for use by the dicitonary
server in the dictd package.

%description -n  %{dictname}-%{dict46}  -l pl
Ten pakiet zawiera s這wnik %{dict46} do u篡wania z serwerem s這wnika
dictd.

%prep
%setup -q -c
%setup -q -c -T -D -a 1
%setup -q -c -T -D -a 2
%setup -q -c -T -D -a 3
%setup -q -c -T -D -a 4
%setup -q -c -T -D -a 5
%setup -q -c -T -D -a 6
%setup -q -c -T -D -a 7
%setup -q -c -T -D -a 8
%setup -q -c -T -D -a 9
%setup -q -c -T -D -a 10
%setup -q -c -T -D -a 11
%setup -q -c -T -D -a 12
#%setup -q -c -T -D -a 13
%setup -q -c -T -D -a 14
%setup -q -c -T -D -a 15
%setup -q -c -T -D -a 16
%setup -q -c -T -D -a 17
%setup -q -c -T -D -a 18
%setup -q -c -T -D -a 19
%setup -q -c -T -D -a 20
%setup -q -c -T -D -a 21
%setup -q -c -T -D -a 22
%setup -q -c -T -D -a 23
%setup -q -c -T -D -a 24
#%setup -q -c -T -D -a 25
%setup -q -c -T -D -a 26
%setup -q -c -T -D -a 27
%setup -q -c -T -D -a 28
%setup -q -c -T -D -a 29
%setup -q -c -T -D -a 30
%setup -q -c -T -D -a 31
%setup -q -c -T -D -a 32
%setup -q -c -T -D -a 33
%setup -q -c -T -D -a 34
%setup -q -c -T -D -a 35
%setup -q -c -T -D -a 36
%setup -q -c -T -D -a 37
%setup -q -c -T -D -a 38
%setup -q -c -T -D -a 39
%setup -q -c -T -D -a 40
%setup -q -c -T -D -a 41
%setup -q -c -T -D -a 42
%setup -q -c -T -D -a 43
%setup -q -c -T -D -a 44
%setup -q -c -T -D -a 45
%setup -q -c -T -D -a 46

%build
cd dictmisc
autoconf
%configure 
%{__make}
cd ..

echo "Making %{dictionaries}"
for i in %{dictionaries}; do
    mv $i.dict.dz $i.gz
    gunzip $i.gz
    dictfiles=%{_datadir}/dictd/%{dictname}-$i
    ./dictmisc/dictfmt -f -u "%{URL}" -s "$i Freedict dictionary" %{dictname}_$i < $i
    dictzip %{dictname}_$i.dict
done


%install
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}

for i in %{dictionaries}; do
    dictprefix=%{_datadir}/dictd/%{dictname}_$i
    echo "# The Bilingual dictionaries
    database $i {
        data  \"$dictprefix.dict.dz\"
        index \"$dictprefix.index\" 
    }
    " > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
    mv %{dictname}_$i*  $RPM_BUILD_ROOT%{_datadir}/dictd/
done

%clean
rm -rf $RPM_BUILD_ROOT

%postun 
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n  %{dictname}-%{dict1}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict1}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi

%postun -n  %{dictname}-%{dict2}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict2}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict3}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict3}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict4}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict4}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict5}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict5}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict6}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict6}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict7}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict7}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict8}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict8}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict9}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict9}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict10}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict10}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict11}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict11}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict12}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict12}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict13}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict13}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict14}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict14}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict15}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict15}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict16}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict16}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict17}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict17}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict18}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict18}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict19}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict19}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict20}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict20}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict21}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict21}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict22}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict22}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict23}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict23}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict24}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict24}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict25}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict25}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict26}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict26}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict27}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict27}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict28}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict28}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict29}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict29}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict30}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict30}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict31}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict31}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict32}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict32}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict33}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict33}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict34}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict34}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict35}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict35}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict36}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict36}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict37}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict37}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict38}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict38}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict39}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict39}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict40}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict40}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict41}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict41}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict42}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict42}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict43}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict43}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict44}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict44}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict45}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict45}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun -n  %{dictname}-%{dict46}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post -n  %{dictname}-%{dict46}
   if [ -f /var/lock/subsys/dictd ]; then
   /etc/rc.d/init.d/dictd restart 1>&2
fi

%files
%defattr(644,root,root,755)

%files -n  %{dictname}-%{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict1}*

%files -n  %{dictname}-%{dict2}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict2}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict2}*

%files -n  %{dictname}-%{dict3}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict3}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict3}*

%files -n  %{dictname}-%{dict4}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict4}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict4}*

%files -n  %{dictname}-%{dict5}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict5}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict5}*

%files -n  %{dictname}-%{dict6}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict6}*

%files -n  %{dictname}-%{dict7}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict7}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict7}*

%files -n  %{dictname}-%{dict8}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict8}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict8}*

%files -n  %{dictname}-%{dict9}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict9}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict9}*

%files -n  %{dictname}-%{dict10}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict10}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict10}*

%files -n  %{dictname}-%{dict11}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict11}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict11}*

%files -n  %{dictname}-%{dict12}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict12}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict12}*

#%files -n  %{dictname}-%{dict13}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict13}.dictconf 
#%{_datadir}/dictd/%{dictname}_%{dict13}*

%files -n  %{dictname}-%{dict14}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict14}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict14}*

%files -n  %{dictname}-%{dict15}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict15}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict15}*

%files -n  %{dictname}-%{dict16}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict16}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict16}*

%files -n  %{dictname}-%{dict17}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict17}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict17}*

%files -n  %{dictname}-%{dict18}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict18}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict18}*

%files -n  %{dictname}-%{dict19}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict19}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict19}*

%files -n  %{dictname}-%{dict20}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict20}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict20}*

%files -n  %{dictname}-%{dict21}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict21}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict21}*

%files -n  %{dictname}-%{dict22}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict22}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict22}*

%files -n  %{dictname}-%{dict23}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict23}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict23}*

%files -n  %{dictname}-%{dict24}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict24}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict24}*

#%files -n  %{dictname}-%{dict25}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict25}.dictconf 
#%{_datadir}/dictd/%{dictname}_%{dict25}*

%files -n  %{dictname}-%{dict26}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict26}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict26}*

%files -n  %{dictname}-%{dict27}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict27}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict27}*

%files -n  %{dictname}-%{dict28}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict28}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict28}*

#%files -n  %{dictname}-%{dict29}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict29}.dictconf 
#%{_datadir}/dictd/%{dictname}_%{dict29}*

%files -n  %{dictname}-%{dict30}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict30}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict30}*

%files -n  %{dictname}-%{dict31}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict31}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict31}*

%files -n  %{dictname}-%{dict32}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict32}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict32}*

%files -n  %{dictname}-%{dict33}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict33}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict33}*

%files -n  %{dictname}-%{dict34}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict34}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict34}*

%files -n  %{dictname}-%{dict35}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict35}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict35}*

%files -n  %{dictname}-%{dict36}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict36}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict36}*

%files -n  %{dictname}-%{dict37}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict37}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict37}*

%files -n  %{dictname}-%{dict38}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict38}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict38}*

%files -n  %{dictname}-%{dict39}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict39}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict39}*

%files -n  %{dictname}-%{dict40}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict40}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict40}*

%files -n  %{dictname}-%{dict41}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict41}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict41}*

%files -n  %{dictname}-%{dict42}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict42}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict42}*

%files -n  %{dictname}-%{dict43}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict43}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict43}*

%files -n  %{dictname}-%{dict44}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict44}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict44}*

%files -n  %{dictname}-%{dict45}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict45}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict45}*

%files -n  %{dictname}-%{dict46}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict46}.dictconf 
%{_datadir}/dictd/%{dictname}_%{dict46}*
