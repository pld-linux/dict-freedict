#
# NOTE: it buildrequires en_IN.UTF-8 locale support in libc
#
%define	dictname	freedict
%define	dict0	afr-deu
%define	dict1	afr-eng
%define	dict2	cze-eng
%define	dict3	dan-eng
%define	dict4	deu-eng
%define	dict5	deu-fra
%define	dict6	deu-ita
%define	dict7	deu-nld
%define	dict8	deu-por
%define	dict9	eng-afr
# empty
#%%define	dict10	eng-cze
%define	dict11	eng-deu
%define	dict12	eng-fra
%define	dict13	eng-hun
%define	dict14	eng-iri
%define	dict15	eng-ita
%define	dict16	eng-lat
%define	dict17	eng-nld
%define	dict18	eng-por
%define	dict19	eng-rom
%define	dict20	eng-rus
%define	dict21	eng-scr
%define	dict22	eng-spa
%define	dict23	eng-swe
%define	dict24	eng-wel
%define	dict25	fra-deu
%define	dict26	fra-eng
%define	dict27	fra-nld
# empty
#%%define	dict28	gre-deu
%define	dict29	hun-eng
%define	dict30	iri-eng
%define	dict31	ita-deu
%define	dict32	ita-eng
%define	dict33	jpn-deu
%define	dict34	kha-deu
%define	dict35	lat-deu
%define	dict36	lat-eng
%define	dict37	nld-deu
%define	dict38	nld-eng
%define	dict39	nld-fra
%define	dict40	por-deu
%define	dict41	por-eng
%define	dict42	sco-deu
%define	dict43	scr-eng
%define	dict44	slo-eng
%define	dict45	spa-eng
%define	dict46	swa-eng
%define	dict47	swe-eng
%define	dict48	tur-deu
%define	dict49	tur-eng
%define	dict50	wel-eng
%define dict51	eng-ara
# empty
#%%define	dict52	eng-hin

%define dicts0	%{dict0}  %{dict1}  %{dict2}  %{dict3}  %{dict4}  %{dict5}  %{dict6}
%define dicts1	%{dict7}  %{dict8}  %{dict9}  %{dict11} %{dict12}
%define dicts2	          %{dict15} %{dict16}           %{dict18} %{dict19}
%define dicts3	                    %{dict22} %{dict23} %{dict24} %{dict25}
%define dicts4	%{dict26} %{dict27} %{dict29} %{dict30} %{dict31} %{dict32}
%define dicts5	%{dict33} %{dict34} %{dict35} %{dict36} %{dict37} %{dict38}
%define dicts6	%{dict39} %{dict40} %{dict41} %{dict42} %{dict43} %{dict44}
%define dicts7	%{dict45} %{dict46} %{dict47} %{dict48} %{dict49}

%define dictionaries %{dicts0} %{dicts1} %{dicts2} %{dicts3} %{dicts4} %{dicts5} %{dicts6} %{dicts7}

Summary:	The free bilingual dictionaries for dictd
Summary(pl.UTF-8):   Darmowe dwujęzykowe słowniki dla dictd
Name:		dict-%{dictname}
Version:	20030508
Release:	3
License:	GPL
Group:		Applications/Dictionaries
# also at ftp://ftp.sourceforge.net/pub/sourceforge/freedict/ if following wouldn't work
Source0:	http://freedict.sourceforge.net/download/linux/%{dict0}.tar.gz
# Source0-md5:	9db57d2971a46aae785f0eac5bdbbc77
Source1:	http://freedict.sourceforge.net/download/linux/%{dict1}.tar.gz
# Source1-md5:	937d6e25e37ce2f913cadff2fafe8850
Source2:	http://freedict.sourceforge.net/download/linux/%{dict2}.tar.gz
# Source2-md5:	39456b7d9e65d86562e35ff883650306
Source3:	http://freedict.sourceforge.net/download/linux/%{dict3}.tar.gz
# Source3-md5:	b665b547785e8537e7dba391fc348f86
Source4:	http://freedict.sourceforge.net/download/linux/%{dict4}.tar.gz
# Source4-md5:	bbf0e8012d01dc9b115babc1f434e7ec
Source5:	http://freedict.sourceforge.net/download/linux/%{dict5}.tar.gz
# Source5-md5:	4428cffc763a22fd64670860705f2ecd
Source6:	http://freedict.sourceforge.net/download/linux/%{dict6}.tar.gz
# Source6-md5:	39af0789c8acad3c12e6e6644e316ba3
Source7:	http://freedict.sourceforge.net/download/linux/%{dict7}.tar.gz
# Source7-md5:	ea024dbd060aaa22a47aa6ce986909df
Source8:	http://freedict.sourceforge.net/download/linux/%{dict8}.tar.gz
# Source8-md5:	06ffcf776daca6c0357cd87f1a3b7bd0
Source9:	http://freedict.sourceforge.net/download/linux/%{dict9}.tar.gz
# Source9-md5:	28a99edfcbbce29d6cbe41c75a8ec220
#
#Source10:	http://freedict.sourceforge.net/download/linux/%{dict10}.tar.gz
#
Source11:	http://freedict.sourceforge.net/download/linux/%{dict11}.tar.gz
# Source11-md5:	809c29221fbed11606ad4e68de11486e
Source12:	http://freedict.sourceforge.net/download/linux/%{dict12}.tar.gz
# Source12-md5:	ec3c73b204e063f6dc38236aa81abbe6
# eng-hun dictionary has been cleared, use the old one from distfiles
Source13:	%{dict13}.tar.gz
# Source13-md5:	3b832ced009d37cddb3ce939db6ed9b5
Source14:	http://freedict.sourceforge.net/download/linux/%{dict14}.tar.gz
# Source14-md5:	0551a4d85173246fc177f065255a1a21
Source15:	http://freedict.sourceforge.net/download/linux/%{dict15}.tar.gz
# Source15-md5:	f4e691e3d81812790f68ab39bda37d58
Source16:	http://freedict.sourceforge.net/download/linux/%{dict16}.tar.gz
# Source16-md5:	d3768f805c3b2cc26a55bab49972abbe
Source17:	http://freedict.sourceforge.net/download/linux/%{dict17}.tar.gz
# Source17-md5:	7f2a4c000772823a6256ded0598dff2a
# eng-por dictionary has been cleared, use the very old one from below
Source18:	http://dl.sourceforge.net/freedict/%{dict18}.tar.gz
# Source18-md5:	736df42657b4daa24c22cba1bfaf6627
Source19:	http://freedict.sourceforge.net/download/linux/%{dict19}.tar.gz
# Source19-md5:	bc2d7605c53adfaeb3e27acf2cc24c76
Source20:	http://freedict.sourceforge.net/download/linux/%{dict20}.tar.gz
# Source20-md5:	8bd97526578de169bf7560a28085b137
Source21:	http://freedict.sourceforge.net/download/linux/%{dict21}.tar.gz
# Source21-md5:	78a390033378196e581cfe3c2040b7ec
Source22:	http://freedict.sourceforge.net/download/linux/%{dict22}.tar.gz
# Source22-md5:	2d2d98226c6ce671e8f7a4f682d94ad8
Source23:	http://freedict.sourceforge.net/download/linux/%{dict23}.tar.gz
# Source23-md5:	a5a5ec7190baeb8acc49e78cee75da87
Source24:	http://freedict.sourceforge.net/download/linux/%{dict24}.tar.gz
# Source24-md5:	834add94422d4efea62db8e6b2157ec3
Source25:	http://freedict.sourceforge.net/download/linux/%{dict25}.tar.gz
# Source25-md5:	e776f0b40e4aa586291e01527a82fe94
Source26:	http://freedict.sourceforge.net/download/linux/%{dict26}.tar.gz
# Source26-md5:	5258048c067f1b2c0b7b471f781c3d68
Source27:	http://freedict.sourceforge.net/download/linux/%{dict27}.tar.gz
# Source27-md5:	07623e0729230c25352a109a8286a6bf
#
#Source28:	http://freedict.sourceforge.net/download/linux/%{dict28}.tar.gz
#
# hun-eng dictionary has been cleared, use the old one from distfiles
Source29:	%{dict29}.tar.gz
# Source29-md5:	9c31a5e39cd08e940550956b10ec3fe2
Source30:	http://freedict.sourceforge.net/download/linux/%{dict30}.tar.gz
# Source30-md5:	1fb5e17b8a181cac525e3a60226c1723
Source31:	http://freedict.sourceforge.net/download/linux/%{dict31}.tar.gz
# Source31-md5:	177b7288655f9b0b0dd556ece5e6fa15
Source32:	http://freedict.sourceforge.net/download/linux/%{dict32}.tar.gz
# Source32-md5:	85113c62955a6aa1d2e0143f57b2335e
Source33:	http://freedict.sourceforge.net/download/linux/%{dict33}.tar.gz
# Source33-md5:	907f394e8bd8d1047d1c76c3852326b7
Source34:	http://freedict.sourceforge.net/download/linux/%{dict34}.tar.gz
# Source34-md5:	31c450a0f63e51e157cac9c1e99173d6
Source35:	http://freedict.sourceforge.net/download/linux/%{dict35}.tar.gz
# Source35-md5:	c1496c442d3d082d0035fcb898aec2ee
Source36:	http://freedict.sourceforge.net/download/linux/%{dict36}.tar.gz
# Source36-md5:	e94cd171a985544870b2912f19329528
Source37:	http://freedict.sourceforge.net/download/linux/%{dict37}.tar.gz
# Source37-md5:	9706807ef14fc3575bd0d07c14840fdf
Source38:	http://freedict.sourceforge.net/download/linux/%{dict38}.tar.gz
# Source38-md5:	0f930af989040d5cc7c58762c0bb86bd
Source39:	http://freedict.sourceforge.net/download/linux/%{dict39}.tar.gz
# Source39-md5:	a215fa3997010e0b3dcae9bc62eb28d6
Source40:	http://freedict.sourceforge.net/download/linux/%{dict40}.tar.gz
# Source40-md5:	fbd66fb9e7d5ca171034d4fdfced36b2
Source41:	http://freedict.sourceforge.net/download/linux/%{dict41}.tar.gz
# Source41-md5:	747ecd61d032d4db7b527b969c7b840f
Source42:	http://freedict.sourceforge.net/download/linux/%{dict42}.tar.gz
# Source42-md5:	288a9bf9a18012161551ac07c5918b5f
Source43:	http://freedict.sourceforge.net/download/linux/%{dict43}.tar.gz
# Source43-md5:	79fda6bb966ca4364016d47fdadbf878
Source44:	http://freedict.sourceforge.net/download/linux/%{dict44}.tar.gz
# Source44-md5:	9dbd9fdf930f2c2c9ac7bc04c8ce6d8d
Source45:	http://freedict.sourceforge.net/download/linux/%{dict45}.tar.gz
# Source45-md5:	61c67a982d1fd6c6b3013ec107e5cd97
Source46:	http://freedict.sourceforge.net/download/linux/%{dict46}.tar.gz
# Source46-md5:	1d5f74d1cbc1fd75617b58bd75ad3736
Source47:	http://freedict.sourceforge.net/download/linux/%{dict47}.tar.gz
# Source47-md5:	eef9b7f6d051a65d303fe31fb9fbb130
Source48:	http://freedict.sourceforge.net/download/linux/%{dict48}.tar.gz
# Source48-md5:	fa7d94cfe2a83c10b443feaefececf43
Source49:	http://freedict.sourceforge.net/download/linux/%{dict49}.tar.gz
# Source49-md5:	db95c621461833fd86aedd6b3d890737
Source50:	http://freedict.sourceforge.net/download/linux/%{dict50}.tar.gz
# Source50-md5:	0ce05d01b7241578388ac69f8d6cb332
Source51:	http://freedict.sourceforge.net/download/linux/%{dict51}.tar.gz
# Source51-md5:	53f0ee3e6127de242280801ef5c00d51
#
#Source52:	http://freedict.sourceforge.net/download/linux/%{dict52}.tar.gz
#
URL:		http://www.freedict.de/
BuildRequires:	dictfmt
BuildRequires:	dictzip
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the free bilingual dictionaries, version
%{version} formatted for use by the dictionary server in the dictd
package.

%description -l pl.UTF-8
Ten pakiet zawiera darmowe dwujęzyczne słowniki w wersji %{version}
sformatowane do użytku z serwerem słownika dictd.

%package %{dict0}
Summary:	The %{dict0} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict0} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict0}
This package contains %{dict0} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict0} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict0} do używania z serwerem słownika
dictd.

%package %{dict1}
Summary:	The %{dict1} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict1} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict1}
This package contains %{dict1} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict1} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict1} do używania z serwerem słownika
dictd.

%package %{dict2}
Summary:	The %{dict2} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict2} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict2}
This package contains %{dict2} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict2} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict2} do używania z serwerem słownika
dictd.

%package %{dict3}
Summary:	The %{dict3} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict3} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict3}
This package contains %{dict3} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict3} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict3} do używania z serwerem słownika
dictd.

%package %{dict4}
Summary:	The %{dict4} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict4} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict4}
This package contains %{dict4} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict4} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict4} do używania z serwerem słownika
dictd.

%package %{dict5}
Summary:	The %{dict5} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict5} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict5}
This package contains %{dict5} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict5} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict5} do używania z serwerem słownika
dictd.

%package %{dict6}
Summary:	The %{dict6} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict6} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict6}
This package contains %{dict6} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict6} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict6} do używania z serwerem słownika
dictd.

%package %{dict7}
Summary:	The %{dict7} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict7} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict7}
This package contains %{dict7} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict7} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict7} do używania z serwerem słownika
dictd.

%package %{dict8}
Summary:	The %{dict8} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict8} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict8}
This package contains %{dict8} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict8} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict8} do używania z serwerem słownika
dictd.

%package %{dict9}
Summary:	The %{dict9} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict9} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict9}
This package contains %{dict9} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict9} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict9} do używania z serwerem słownika
dictd.

%package %{dict10}
Summary:	The %{dict10} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict10} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict10}
This package contains %{dict10} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict10} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict10} do używania z serwerem słownika
dictd.

%package %{dict11}
Summary:	The %{dict11} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict11} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict11}
This package contains %{dict11} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict11} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict11} do używania z serwerem słownika
dictd.

%package %{dict12}
Summary:	The %{dict12} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict12} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict12}
This package contains %{dict12} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict12} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict12} do używania z serwerem słownika
dictd.

%package %{dict13}
Summary:	The %{dict13} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict13} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict13}
This package contains %{dict13} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict13} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict13} do używania z serwerem słownika
dictd.

%package %{dict14}
Summary:	The %{dict14} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict14} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict14}
This package contains %{dict14} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict14} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict14} do używania z serwerem słownika
dictd.

%package %{dict15}
Summary:	The %{dict15} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict15} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict15}
This package contains %{dict15} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict15} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict15} do używania z serwerem słownika
dictd.

%package %{dict16}
Summary:	The %{dict16} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict16} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict16}
This package contains %{dict16} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict16} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict16} do używania z serwerem słownika
dictd.

%package %{dict17}
Summary:	The %{dict17} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict17} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict17}
This package contains %{dict17} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict17} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict17} do używania z serwerem słownika
dictd.

%package %{dict18}
Summary:	The %{dict18} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict18} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict18}
This package contains %{dict18} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict18} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict18} do używania z serwerem słownika
dictd.

%package %{dict19}
Summary:	The %{dict19} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict19} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict19}
This package contains %{dict19} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict19} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict19} do używania z serwerem słownika
dictd.

%package %{dict20}
Summary:	The %{dict20} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict20} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict20}
This package contains %{dict20} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict20} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict20} do używania z serwerem słownika
dictd.

%package %{dict21}
Summary:	The %{dict21} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict21} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict21}
This package contains %{dict21} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict21} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict21} do używania z serwerem słownika
dictd.

%package %{dict22}
Summary:	The %{dict22} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict22} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict22}
This package contains %{dict22} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict22} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict22} do używania z serwerem słownika
dictd.

%package %{dict23}
Summary:	The %{dict23} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict23} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict23}
This package contains %{dict23} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict23} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict23} do używania z serwerem słownika
dictd.

%package %{dict24}
Summary:	The %{dict24} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict24} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict24}
This package contains %{dict24} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict24} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict24} do używania z serwerem słownika
dictd.

%package %{dict25}
Summary:	The %{dict25} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict25} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict25}
This package contains %{dict25} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict25} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict25} do używania z serwerem słownika
dictd.

%package %{dict26}
Summary:	The %{dict26} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict26} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict26}
This package contains %{dict26} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict26} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict26} do używania z serwerem słownika
dictd.

%package %{dict27}
Summary:	The %{dict27} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict27} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict27}
This package contains %{dict27} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict27} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict27} do używania z serwerem słownika
dictd.

%package %{dict28}
Summary:	The %{dict28} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict28} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict28}
This package contains %{dict28} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict28} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict28} do używania z serwerem słownika
dictd.

%package %{dict29}
Summary:	The %{dict29} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict29} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict29}
This package contains %{dict29} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict29} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict29} do używania z serwerem słownika
dictd.

%package %{dict30}
Summary:	The %{dict30} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict30} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict30}
This package contains %{dict30} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict30} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict30} do używania z serwerem słownika
dictd.

%package %{dict31}
Summary:	The %{dict31} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict31} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict31}
This package contains %{dict31} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict31} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict31} do używania z serwerem słownika
dictd.

%package %{dict32}
Summary:	The %{dict32} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict32} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict32}
This package contains %{dict32} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict32} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict32} do używania z serwerem słownika
dictd.

%package %{dict33}
Summary:	The %{dict33} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict33} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict33}
This package contains %{dict33} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict33} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict33} do używania z serwerem słownika
dictd.

%package %{dict34}
Summary:	The %{dict34} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict34} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict34}
This package contains %{dict34} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict34} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict34} do używania z serwerem słownika
dictd.

%package %{dict35}
Summary:	The %{dict35} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict35} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict35}
This package contains %{dict35} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict35} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict35} do używania z serwerem słownika
dictd.

%package %{dict36}
Summary:	The %{dict36} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict36} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict36}
This package contains %{dict36} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict36} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict36} do używania z serwerem słownika
dictd.

%package %{dict37}
Summary:	The %{dict37} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict37} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict37}
This package contains %{dict37} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict37} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict37} do używania z serwerem słownika
dictd.

%package %{dict38}
Summary:	The %{dict38} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict38} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict38}
This package contains %{dict38} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict38} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict38} do używania z serwerem słownika
dictd.

%package %{dict39}
Summary:	The %{dict39} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict39} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict39}
This package contains %{dict39} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict39} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict39} do używania z serwerem słownika
dictd.

%package %{dict40}
Summary:	The %{dict40} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict40} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict40}
This package contains %{dict40} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict40} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict40} do używania z serwerem słownika
dictd.

%package %{dict41}
Summary:	The %{dict41} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict41} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict41}
This package contains %{dict41} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict41} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict41} do używania z serwerem słownika
dictd.

%package %{dict42}
Summary:	The %{dict42} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict42} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict42}
This package contains %{dict42} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict42} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict42} do używania z serwerem słownika
dictd.

%package %{dict43}
Summary:	The %{dict43} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict43} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict43}
This package contains %{dict43} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict43} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict43} do używania z serwerem słownika
dictd.

%package %{dict44}
Summary:	The %{dict44} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict44} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict44}
This package contains %{dict44} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict44} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict44} do używania z serwerem słownika
dictd.

%package %{dict45}
Summary:	The %{dict45} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict45} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict45}
This package contains %{dict45} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict45} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict45} do używania z serwerem słownika
dictd.

%package %{dict46}
Summary:	The %{dict46} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict46} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict46}
This package contains %{dict46} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict46} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict46} do używania z serwerem słownika
dictd.

%package %{dict47}
Summary:	The %{dict47} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict47} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict47}
This package contains %{dict47} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict47} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict47} do używania z serwerem słownika
dictd.

%package %{dict48}
Summary:	The %{dict48} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict48} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict48}
This package contains %{dict48} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict48} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict48} do używania z serwerem słownika
dictd.

%package %{dict49}
Summary:	The %{dict49} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict49} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict49}
This package contains %{dict49} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict49} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict49} do używania z serwerem słownika
dictd.

%package %{dict50}
Summary:	The %{dict50} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict50} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict50}
This package contains %{dict50} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict50} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict50} do używania z serwerem słownika
dictd.

%package %{dict51}
Summary:	The %{dict51} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict51} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict51}
This package contains %{dict51} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict51} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict51} do używania z serwerem słownika
dictd.

%package %{dict52}
Summary:	The %{dict52} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict52} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict52}
This package contains %{dict52} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict52} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict52} do używania z serwerem słownika
dictd.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51
# temporarily removed: -a10 -a28 -a52

%build
echo "Making %{dictionaries}"
for i in %{dictionaries}; do
	mv $i.dict.dz $i.gz
	gunzip $i.gz
	dictfmt -f -u "%url" -s "$i Freedict dictionary" %{dictname}_$i --locale en_IN.UTF-8 < $i
	dictzip %{dictname}_$i.dict
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

for i in %{dictionaries}; do
	dictprefix=%{_datadir}/dictd/%{dictname}_$i
	echo "# The Bilingual dictionaries
database $i {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
	mv %{dictname}_$i.* $RPM_BUILD_ROOT%{_datadir}/dictd
done

%clean
rm -rf $RPM_BUILD_ROOT

%post %{dict0}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict0}
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

%post %{dict47}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict47}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict48}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict48}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict49}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict49}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict50}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict50}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict51}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict51}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict52}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict52}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files %{dict0}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict0}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict0}.*

%files %{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict1}.*

%files %{dict2}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict2}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict2}.*

%files %{dict3}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict3}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict3}.*

%files %{dict4}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict4}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict4}.*

%files %{dict5}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict5}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict5}.*

%files %{dict6}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict6}.*

%files %{dict7}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict7}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict7}.*

%files %{dict8}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict8}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict8}.*

%files %{dict9}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict9}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict9}.*

#%files %{dict10}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict10}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict10}.*

%files %{dict11}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict11}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict11}.*

%files %{dict12}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict12}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict12}.*

#%files %{dict13}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict13}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict13}.*

#%files %{dict14}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict14}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict14}.*

%files %{dict15}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict15}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict15}.*

%files %{dict16}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict16}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict16}.*

#%files %{dict17}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict17}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict17}.*

%files %{dict18}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict18}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict18}.*

%files %{dict19}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict19}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict19}.*

#%files %{dict20}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict20}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict20}.*

#%files %{dict21}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict21}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict21}.*

%files %{dict22}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict22}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict22}.*

%files %{dict23}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict23}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict23}.*

%files %{dict24}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict24}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict24}.*

%files %{dict25}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict25}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict25}.*

%files %{dict26}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict26}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict26}.*

%files %{dict27}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict27}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict27}.*

#%files %{dict28}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict28}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict28}.*

%files %{dict29}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict29}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict29}.*

%files %{dict30}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict30}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict30}.*

%files %{dict31}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict31}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict31}.*

%files %{dict32}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict32}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict32}.*

%files %{dict33}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict33}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict33}.*

%files %{dict34}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict34}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict34}.*

%files %{dict35}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict35}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict35}.*

%files %{dict36}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict36}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict36}.*

%files %{dict37}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict37}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict37}.*

%files %{dict38}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict38}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict38}.*

%files %{dict39}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict39}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict39}.*

%files %{dict40}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict40}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict40}.*

%files %{dict41}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict41}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict41}.*

%files %{dict42}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict42}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict42}.*

%files %{dict43}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict43}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict43}.*

%files %{dict44}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict44}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict44}.*

%files %{dict45}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict45}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict45}.*

%files %{dict46}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict46}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict46}.*

%files %{dict47}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict47}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict47}.*

%files %{dict48}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict48}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict48}.*

%files %{dict49}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict49}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict49}.*

#%files %{dict50}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict50}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict50}.*

#%files %{dict51}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict51}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict51}.*

#%files %{dict52}
#%defattr(644,root,root,755)
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict52}.dictconf
#%{_datadir}/dictd/%{dictname}_%{dict52}.*
