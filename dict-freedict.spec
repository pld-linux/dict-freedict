%define	dictname	freedict
%define	dict1	afr-deu
%define	dict2	cze-eng
%define	dict3	dan-eng
%define	dict4	deu-eng
%define	dict5 	deu-fra
%define	dict6	deu-ita
%define	dict7	deu-nld
%define	dict8 	deu-por
%define	dict9 	eng-deu
%define	dict10	eng-fra
%define	dict11	eng-hun
%define	dict12	eng-iri
%define	dict13	eng-ita
%define	dict14	eng-lat
%define	dict15	eng-nld
%define	dict16	eng-por
%define	dict17	eng-rus
%define	dict18	eng-scr
%define	dict19	eng-spa
%define	dict20	eng-swe
%define	dict21	eng-wel
%define	dict22	fra-deu
%define	dict23	fra-eng
%define	dict24	fra-nld
# empty
%define	dict25	gre-deu
%define	dict26	hun-eng
%define	dict27	iri-eng
%define	dict28	ita-deu
# not present
%define	dict29	ita-eng
%define	dict30	jpn-deu
%define	dict31	lat-deu
%define	dict32	lat-eng
%define	dict33	nld-deu
%define	dict34	nld-eng
%define	dict35	nld-fra
%define	dict36	por-deu
%define	dict37	por-eng
%define	dict38	sco-deu
%define	dict39	scr-eng
%define	dict40	slo-eng
%define	dict41	spa-eng
%define	dict42	swa-eng
%define	dict43	swe-eng
%define	dict44	tur-deu
%define	dict45	tur-eng
%define	dict46	wel-eng
# removed dict25 dict29 --undefine's patch.
%define dictionaries %{dict1} %{dict2} %{dict3} %{dict4} %{dict5} %{dict6} %{dict7} %{dict8} %{dict9} %{dict10} %{dict11} %{dict12} %{dict13} %{dict14} %{dict15} %{dict16} %{dict17} %{dict18} %{dict19} %{dict20} %{dict21} %{dict22} %{dict23} %{dict24} %{dict26} %{dict27} %{dict28} %{dict30} %{dict31} %{dict32} %{dict33} %{dict34} %{dict35} %{dict36} %{dict37} %{dict38} %{dict39} %{dict40} %{dict41} %{dict42} %{dict43} %{dict44} %{dict45} %{dict46}

Summary:	The Free bilingual dictionaries for dictd
Summary(pl):	Darmowe dwuj瞛ykowe S這wniki dla dictd
Name:		dict-%{dictname}
Version:	20020622
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://www.freedict.de/download/linux/dictmisc.tar.gz
# also at ftp://ftp.sourceforge.net/pub/sourceforge/freedict/ if following wouldn't work
Source1:	http://freedict.sourceforge.net/download/linux/%{dict1}.tar.gz
Source2:	http://freedict.sourceforge.net/download/linux/%{dict2}.tar.gz
Source3:	http://freedict.sourceforge.net/download/linux/%{dict3}.tar.gz
Source4:	http://freedict.sourceforge.net/download/linux/%{dict4}.tar.gz
Source5:	http://freedict.sourceforge.net/download/linux/%{dict5}.tar.gz
Source6:	http://freedict.sourceforge.net/download/linux/%{dict6}.tar.gz
Source7:	http://freedict.sourceforge.net/download/linux/%{dict7}.tar.gz
Source8:	http://freedict.sourceforge.net/download/linux/%{dict8}.tar.gz
Source9:	http://freedict.sourceforge.net/download/linux/%{dict9}.tar.gz
Source10:	http://freedict.sourceforge.net/download/linux/%{dict10}.tar.gz
Source11:	http://freedict.sourceforge.net/download/linux/%{dict11}.tar.gz
Source12:	http://freedict.sourceforge.net/download/linux/%{dict12}.tar.gz
Source13:	http://freedict.sourceforge.net/download/linux/%{dict13}.tar.gz
Source14:	http://freedict.sourceforge.net/download/linux/%{dict14}.tar.gz
Source15:	http://freedict.sourceforge.net/download/linux/%{dict15}.tar.gz
Source16:	http://freedict.sourceforge.net/download/linux/%{dict16}.tar.gz
Source17:	http://freedict.sourceforge.net/download/linux/%{dict17}.tar.gz
Source18:	http://freedict.sourceforge.net/download/linux/%{dict18}.tar.gz
Source19:	http://freedict.sourceforge.net/download/linux/%{dict19}.tar.gz
Source20:	http://freedict.sourceforge.net/download/linux/%{dict20}.tar.gz
Source21:	http://freedict.sourceforge.net/download/linux/%{dict21}.tar.gz
Source22:	http://freedict.sourceforge.net/download/linux/%{dict22}.tar.gz
Source23:	http://freedict.sourceforge.net/download/linux/%{dict23}.tar.gz
Source24:	http://freedict.sourceforge.net/download/linux/%{dict24}.tar.gz
Source25:	http://freedict.sourceforge.net/download/linux/%{dict25}.tar.gz
Source26:	http://freedict.sourceforge.net/download/linux/%{dict26}.tar.gz
Source27:	http://freedict.sourceforge.net/download/linux/%{dict27}.tar.gz
Source28:	http://freedict.sourceforge.net/download/linux/%{dict28}.tar.gz
#Source29:	http://freedict.sourceforge.net/download/linux/%{dict29}.tar.gz
Source30:	http://freedict.sourceforge.net/download/linux/%{dict30}.tar.gz
Source31:	http://freedict.sourceforge.net/download/linux/%{dict31}.tar.gz
Source32:	http://freedict.sourceforge.net/download/linux/%{dict32}.tar.gz
Source33:	http://freedict.sourceforge.net/download/linux/%{dict33}.tar.gz
Source34:	http://freedict.sourceforge.net/download/linux/%{dict34}.tar.gz
Source35:	http://freedict.sourceforge.net/download/linux/%{dict35}.tar.gz
Source36:	http://freedict.sourceforge.net/download/linux/%{dict36}.tar.gz
Source37:	http://freedict.sourceforge.net/download/linux/%{dict37}.tar.gz
Source38:	http://freedict.sourceforge.net/download/linux/%{dict38}.tar.gz
Source39:	http://freedict.sourceforge.net/download/linux/%{dict39}.tar.gz
Source40:	http://freedict.sourceforge.net/download/linux/%{dict40}.tar.gz
Source41:	http://freedict.sourceforge.net/download/linux/%{dict41}.tar.gz
Source42:	http://freedict.sourceforge.net/download/linux/%{dict42}.tar.gz
Source43:	http://freedict.sourceforge.net/download/linux/%{dict43}.tar.gz
Source44:	http://freedict.sourceforge.net/download/linux/%{dict44}.tar.gz
Source45:	http://freedict.sourceforge.net/download/linux/%{dict45}.tar.gz
Source46:	http://freedict.sourceforge.net/download/linux/%{dict46}.tar.gz
URL:		http://www.freedict.de/
BuildRequires:	autoconf
BuildRequires:	dictzip
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains The The Free bilingual dictionaries, version
%version formatted for use by the dictionary server in the dictd
package.

%description -l pl
Ten pakiet zawiera darmowe dwuj瞛yczne s這wniki w wersji %version
sformatowane do u篡tku z serwerem s這wnika dictd.

%package %{dict1}
Summary:	The %{dict1} Dictionary for dictd
Summary(pl):	S這wnik %{dict1} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict1}
This package contains %{dict1} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict1} -l pl
Ten pakiet zawiera s這wnik %{dict1} do u篡wania z serwerem s這wnika
dictd.

%package %{dict2}
Summary:	The %{dict2} Dictionary for dictd
Summary(pl):	S這wnik %{dict2} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict2}
This package contains %{dict2} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict2} -l pl
Ten pakiet zawiera s這wnik %{dict2} do u篡wania z serwerem s這wnika
dictd.

%package %{dict3}
Summary:	The %{dict3} Dictionary for dictd
Summary(pl):	S這wnik %{dict3} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict3}
This package contains %{dict3} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict3} -l pl
Ten pakiet zawiera s這wnik %{dict3} do u篡wania z serwerem s這wnika
dictd.

%package %{dict4}
Summary:	The %{dict4} Dictionary for dictd
Summary(pl):	S這wnik %{dict4} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict4}
This package contains %{dict4} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict4} -l pl
Ten pakiet zawiera s這wnik %{dict4} do u篡wania z serwerem s這wnika
dictd.

%package %{dict5}
Summary:	The %{dict5} Dictionary for dictd
Summary(pl):	S這wnik %{dict5} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict5}
This package contains %{dict5} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict5} -l pl
Ten pakiet zawiera s這wnik %{dict5} do u篡wania z serwerem s這wnika
dictd.

%package %{dict6}
Summary:	The %{dict6} Dictionary for dictd
Summary(pl):	S這wnik %{dict6} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict6}
This package contains %{dict6} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict6} -l pl
Ten pakiet zawiera s這wnik %{dict6} do u篡wania z serwerem s這wnika
dictd.

%package %{dict7}
Summary:	The %{dict7} Dictionary for dictd
Summary(pl):	S這wnik %{dict7} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict7}
This package contains %{dict7} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict7} -l pl
Ten pakiet zawiera s這wnik %{dict7} do u篡wania z serwerem s這wnika
dictd.

%package %{dict8}
Summary:	The %{dict8} Dictionary for dictd
Summary(pl):	S這wnik %{dict8} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict8}
This package contains %{dict8} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict8} -l pl
Ten pakiet zawiera s這wnik %{dict8} do u篡wania z serwerem s這wnika
dictd.

%package %{dict9}
Summary:	The %{dict9} Dictionary for dictd
Summary(pl):	S這wnik %{dict9} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict9}
This package contains %{dict9} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict9} -l pl
Ten pakiet zawiera s這wnik %{dict9} do u篡wania z serwerem s這wnika
dictd.

%package %{dict10}
Summary:	The %{dict10} Dictionary for dictd
Summary(pl):	S這wnik %{dict10} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict10}
This package contains %{dict10} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict10} -l pl
Ten pakiet zawiera s這wnik %{dict10} do u篡wania z serwerem s這wnika
dictd.

%package %{dict11}
Summary:	The %{dict11} Dictionary for dictd
Summary(pl):	S這wnik %{dict11} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict11}
This package contains %{dict11} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict11} -l pl
Ten pakiet zawiera s這wnik %{dict11} do u篡wania z serwerem s這wnika
dictd.

%package %{dict12}
Summary:	The %{dict12} Dictionary for dictd
Summary(pl):	S這wnik %{dict12} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict12}
This package contains %{dict12} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict12} -l pl
Ten pakiet zawiera s這wnik %{dict12} do u篡wania z serwerem s這wnika
dictd.

%package %{dict13}
Summary:	The %{dict13} Dictionary for dictd
Summary(pl):	S這wnik %{dict13} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict13}
This package contains %{dict13} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict13} -l pl
Ten pakiet zawiera s這wnik %{dict13} do u篡wania z serwerem s這wnika
dictd.

%package %{dict14}
Summary:	The %{dict14} Dictionary for dictd
Summary(pl):	S這wnik %{dict14} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict14}
This package contains %{dict14} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict14} -l pl
Ten pakiet zawiera s這wnik %{dict14} do u篡wania z serwerem s這wnika
dictd.

%package %{dict15}
Summary:	The %{dict15} Dictionary for dictd
Summary(pl):	S這wnik %{dict15} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict15}
This package contains %{dict15} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict15} -l pl
Ten pakiet zawiera s這wnik %{dict15} do u篡wania z serwerem s這wnika
dictd.

%package %{dict16}
Summary:	The %{dict16} Dictionary for dictd
Summary(pl):	S這wnik %{dict16} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict16}
This package contains %{dict16} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict16} -l pl
Ten pakiet zawiera s這wnik %{dict16} do u篡wania z serwerem s這wnika
dictd.

%package %{dict17}
Summary:	The %{dict17} Dictionary for dictd
Summary(pl):	S這wnik %{dict17} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict17}
This package contains %{dict17} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict17} -l pl
Ten pakiet zawiera s這wnik %{dict17} do u篡wania z serwerem s這wnika
dictd.

%package %{dict18}
Summary:	The %{dict18} Dictionary for dictd
Summary(pl):	S這wnik %{dict18} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict18}
This package contains %{dict18} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict18} -l pl
Ten pakiet zawiera s這wnik %{dict18} do u篡wania z serwerem s這wnika
dictd.

%package %{dict19}
Summary:	The %{dict19} Dictionary for dictd
Summary(pl):	S這wnik %{dict19} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict19}
This package contains %{dict19} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict19} -l pl
Ten pakiet zawiera s這wnik %{dict19} do u篡wania z serwerem s這wnika
dictd.

%package %{dict20}
Summary:	The %{dict20} Dictionary for dictd
Summary(pl):	S這wnik %{dict20} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict20}
This package contains %{dict20} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict20} -l pl
Ten pakiet zawiera s這wnik %{dict20} do u篡wania z serwerem s這wnika
dictd.

%package %{dict21}
Summary:	The %{dict21} Dictionary for dictd
Summary(pl):	S這wnik %{dict21} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict21}
This package contains %{dict21} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict21} -l pl
Ten pakiet zawiera s這wnik %{dict21} do u篡wania z serwerem s這wnika
dictd.

%package %{dict22}
Summary:	The %{dict22} Dictionary for dictd
Summary(pl):	S這wnik %{dict22} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict22}
This package contains %{dict22} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict22} -l pl
Ten pakiet zawiera s這wnik %{dict22} do u篡wania z serwerem s這wnika
dictd.

%package %{dict23}
Summary:	The %{dict23} Dictionary for dictd
Summary(pl):	S這wnik %{dict23} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict23}
This package contains %{dict23} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict23} -l pl
Ten pakiet zawiera s這wnik %{dict23} do u篡wania z serwerem s這wnika
dictd.

%package %{dict24}
Summary:	The %{dict24} Dictionary for dictd
Summary(pl):	S這wnik %{dict24} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict24}
This package contains %{dict24} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict24} -l pl
Ten pakiet zawiera s這wnik %{dict24} do u篡wania z serwerem s這wnika
dictd.

%package %{dict25}
Summary:	The %{dict25} Dictionary for dictd
Summary(pl):	S這wnik %{dict25} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict25}
This package contains %{dict25} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict25} -l pl
Ten pakiet zawiera s這wnik %{dict25} do u篡wania z serwerem s這wnika
dictd.

%package %{dict26}
Summary:	The %{dict26} Dictionary for dictd
Summary(pl):	S這wnik %{dict26} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict26}
This package contains %{dict26} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict26} -l pl
Ten pakiet zawiera s這wnik %{dict26} do u篡wania z serwerem s這wnika
dictd.

%package %{dict27}
Summary:	The %{dict27} Dictionary for dictd
Summary(pl):	S這wnik %{dict27} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict27}
This package contains %{dict27} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict27} -l pl
Ten pakiet zawiera s這wnik %{dict27} do u篡wania z serwerem s這wnika
dictd.

%package %{dict28}
Summary:	The %{dict28} Dictionary for dictd
Summary(pl):	S這wnik %{dict28} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict28}
This package contains %{dict28} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict28} -l pl
Ten pakiet zawiera s這wnik %{dict28} do u篡wania z serwerem s這wnika
dictd.

%package %{dict29}
Summary:	The %{dict29} Dictionary for dictd
Summary(pl):	S這wnik %{dict29} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict29}
This package contains %{dict29} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict29} -l pl
Ten pakiet zawiera s這wnik %{dict29} do u篡wania z serwerem s這wnika
dictd.

%package %{dict30}
Summary:	The %{dict30} Dictionary for dictd
Summary(pl):	S這wnik %{dict30} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict30}
This package contains %{dict30} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict30} -l pl
Ten pakiet zawiera s這wnik %{dict30} do u篡wania z serwerem s這wnika
dictd.

%package %{dict31}
Summary:	The %{dict31} Dictionary for dictd
Summary(pl):	S這wnik %{dict31} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict31}
This package contains %{dict31} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict31} -l pl
Ten pakiet zawiera s這wnik %{dict31} do u篡wania z serwerem s這wnika
dictd.

%package %{dict32}
Summary:	The %{dict32} Dictionary for dictd
Summary(pl):	S這wnik %{dict32} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict32}
This package contains %{dict32} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict32} -l pl
Ten pakiet zawiera s這wnik %{dict32} do u篡wania z serwerem s這wnika
dictd.

%package %{dict33}
Summary:	The %{dict33} Dictionary for dictd
Summary(pl):	S這wnik %{dict33} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict33}
This package contains %{dict33} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict33} -l pl
Ten pakiet zawiera s這wnik %{dict33} do u篡wania z serwerem s這wnika
dictd.

%package %{dict34}
Summary:	The %{dict34} Dictionary for dictd
Summary(pl):	S這wnik %{dict34} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict34}
This package contains %{dict34} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict34} -l pl
Ten pakiet zawiera s這wnik %{dict34} do u篡wania z serwerem s這wnika
dictd.

%package %{dict35}
Summary:	The %{dict35} Dictionary for dictd
Summary(pl):	S這wnik %{dict35} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict35}
This package contains %{dict35} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict35} -l pl
Ten pakiet zawiera s這wnik %{dict35} do u篡wania z serwerem s這wnika
dictd.

%package %{dict36}
Summary:	The %{dict36} Dictionary for dictd
Summary(pl):	S這wnik %{dict36} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict36}
This package contains %{dict36} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict36} -l pl
Ten pakiet zawiera s這wnik %{dict36} do u篡wania z serwerem s這wnika
dictd.

%package %{dict37}
Summary:	The %{dict37} Dictionary for dictd
Summary(pl):	S這wnik %{dict37} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict37}
This package contains %{dict37} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict37} -l pl
Ten pakiet zawiera s這wnik %{dict37} do u篡wania z serwerem s這wnika
dictd.

%package %{dict38}
Summary:	The %{dict38} Dictionary for dictd
Summary(pl):	S這wnik %{dict38} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict38}
This package contains %{dict38} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict38} -l pl
Ten pakiet zawiera s這wnik %{dict38} do u篡wania z serwerem s這wnika
dictd.

%package %{dict39}
Summary:	The %{dict39} Dictionary for dictd
Summary(pl):	S這wnik %{dict39} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict39}
This package contains %{dict39} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict39} -l pl
Ten pakiet zawiera s這wnik %{dict39} do u篡wania z serwerem s這wnika
dictd.

%package %{dict40}
Summary:	The %{dict40} Dictionary for dictd
Summary(pl):	S這wnik %{dict40} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict40}
This package contains %{dict40} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict40} -l pl
Ten pakiet zawiera s這wnik %{dict40} do u篡wania z serwerem s這wnika
dictd.

%package %{dict41}
Summary:	The %{dict41} Dictionary for dictd
Summary(pl):	S這wnik %{dict41} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict41}
This package contains %{dict41} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict41} -l pl
Ten pakiet zawiera s這wnik %{dict41} do u篡wania z serwerem s這wnika
dictd.

%package %{dict42}
Summary:	The %{dict42} Dictionary for dictd
Summary(pl):	S這wnik %{dict42} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict42}
This package contains %{dict42} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict42} -l pl
Ten pakiet zawiera s這wnik %{dict42} do u篡wania z serwerem s這wnika
dictd.

%package %{dict43}
Summary:	The %{dict43} Dictionary for dictd
Summary(pl):	S這wnik %{dict43} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict43}
This package contains %{dict43} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict43} -l pl
Ten pakiet zawiera s這wnik %{dict43} do u篡wania z serwerem s這wnika
dictd.

%package %{dict44}
Summary:	The %{dict44} Dictionary for dictd
Summary(pl):	S這wnik %{dict44} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict44}
This package contains %{dict44} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict44} -l pl
Ten pakiet zawiera s這wnik %{dict44} do u篡wania z serwerem s這wnika
dictd.

%package %{dict45}
Summary:	The %{dict45} Dictionary for dictd
Summary(pl):	S這wnik %{dict45} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict45}
This package contains %{dict45} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict45} -l pl
Ten pakiet zawiera s這wnik %{dict45} do u篡wania z serwerem s這wnika
dictd.

%package %{dict46}
Summary:	The %{dict46} Dictionary for dictd
Summary(pl):	S這wnik %{dict46} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict46}
This package contains %{dict46} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict46} -l pl
Ten pakiet zawiera s這wnik %{dict46} do u篡wania z serwerem s這wnika
dictd.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a26 -a27 -a28 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46
# temporarily(?) removed
# -a25 -a29

%build
cd dictmisc
%{__autoconf}
%configure
%{__make}
cd ..

echo "Making %{dictionaries}"
for i in %{dictionaries}; do
  mv $i.dict.dz $i.gz
  gunzip $i.gz
  dictfiles=%{_datadir}/dictd/$i
  ./dictmisc/dictfmt -f -u "%{URL}" -s "$i Freedict dictionary" %{dictname}_$i < $i
  dictzip %{dictname}_$i.dict
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}

for i in %{dictionaries}; do
  dictprefix=%{_datadir}/dictd/%{dictname}_$i
  echo "# The Bilingual dictionaries
database $i {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
  mv %{dictname}_$i.* $RPM_BUILD_ROOT%{_datadir}/dictd/
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict1}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict1}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict2}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict2}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict3}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict3}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict4}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict4}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict5}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict5}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict6}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict6}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict7}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict7}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict8}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict8}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict9}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict9}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict10}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict10}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict11}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict11}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict12}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict12}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict13}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict13}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict14}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict14}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict15}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict15}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict16}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict16}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict17}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict17}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict18}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict18}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict19}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict19}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict20}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict20}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict21}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict21}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict22}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict22}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict23}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict23}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict24}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict24}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict25}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict25}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict26}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict26}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict27}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict27}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict28}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict28}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict29}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict29}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict30}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict30}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict31}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict31}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict32}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict32}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict33}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict33}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict34}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict34}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict35}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict35}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict36}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict36}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict37}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict37}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict38}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict38}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict39}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict39}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict40}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict40}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict41}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict41}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict42}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict42}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict43}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict43}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict44}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict44}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict45}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict45}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict46}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict46}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files %{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict1}.*

%files %{dict2}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict2}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict2}.*

%files %{dict3}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict3}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict3}.*

%files %{dict4}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict4}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict4}.*

%files %{dict5}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict5}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict5}.*

%files %{dict6}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict6}.*

%files %{dict7}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict7}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict7}.*

%files %{dict8}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict8}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict8}.*

%files %{dict9}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict9}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict9}.*

%files %{dict10}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict10}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict10}.*

%files %{dict11}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict11}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict11}.*

%files %{dict12}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict12}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict12}.*

%files %{dict13}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict13}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict13}.*

%files %{dict14}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict14}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict14}.*

%files %{dict15}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict15}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict15}.*

%files %{dict16}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict16}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict16}.*

%files %{dict17}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict17}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict17}.*

%files %{dict18}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict18}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict18}.*

%files %{dict19}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict19}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict19}.*

%files %{dict20}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict20}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict20}.*

%files %{dict21}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict21}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict21}.*

%files %{dict22}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict22}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict22}.*

%files %{dict23}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict23}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict23}.*

%files %{dict24}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict24}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict24}.*

#%files %{dict25}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict25}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict25}.*

%files %{dict26}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict26}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict26}.*

%files %{dict27}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict27}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict27}.*

%files %{dict28}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict28}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict28}.*

#%files %{dict29}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict29}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict29}.*

%files %{dict30}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict30}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict30}.*

%files %{dict31}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict31}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict31}.*

%files %{dict32}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict32}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict32}.*

%files %{dict33}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict33}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict33}.*

%files %{dict34}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict34}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict34}.*

%files %{dict35}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict35}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict35}.*

%files %{dict36}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict36}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict36}.*

%files %{dict37}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict37}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict37}.*

%files %{dict38}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict38}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict38}.*

%files %{dict39}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict39}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict39}.*

%files %{dict40}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict40}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict40}.*

%files %{dict41}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict41}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict41}.*

%files %{dict42}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict42}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict42}.*

%files %{dict43}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict43}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict43}.*

%files %{dict44}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict44}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict44}.*

%files %{dict45}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict45}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict45}.*

%files %{dict46}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict46}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict46}.*
