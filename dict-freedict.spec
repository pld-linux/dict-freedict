%define     dictname    freedict
%define      dict1    afr-deu
%define      dict2    cze-eng
%define      dict3    dan-eng
%define      dict4    deu-eng
%define      dict5    deu-fra
%define      dict6    deu-ita
#%define      dict7    deu-nld
%define      dict8    deu-por
%define      dict9    eng-deu
%define      dict10    eng-fra
%define      dict11    eng-hun
%define      dict12    eng-iri
%define      dict13    eng-ita
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
%define      dictionaries %{dict1} %{dict2} %{dict3} %{dict4} %{dict5} %{dict6} %{dict7} %{dict8} %{dict9} %{dict10} %{dict11} %{dict12} %{dict13} %{dict14} %{dict15} %{dict16} %{dict17} %{dict18} %{dict19} %{dict20} %{dict21} %{dict22} %{dict23} %{dict24} %{dict25} %{dict26} %{dict27} %{dict28} %{dict29} %{dict30} %{dict31} %{dict32} %{dict33} %{dict34} %{dict35} %{dict36} %{dict37} %{dict38} %{dict39} %{dict40} %{dict41} %{dict42} %{dict43} %{dict44} %{dict45} %{dict46}


Summary:	The Free bilingual dictionaries for dictd
Summary(pl):	Darmowe dwuj瞛ykowe S這wniki dla dictd
Name:		%{dictname}
Version:	20020622
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://www.freedict.de/pub/dict/dictmisc.tar.gz
Source1:    http://freedict.sourceforge.net/download/linux/%{dict1}.tar.gz
Source2:    http://freedict.sourceforge.net/download/linux/%{dict2}.tar.gz
Source3:    http://freedict.sourceforge.net/download/linux/%{dict3}.tar.gz
Source4:    http://freedict.sourceforge.net/download/linux/%{dict4}.tar.gz
Source5:    http://freedict.sourceforge.net/download/linux/%{dict5}.tar.gz
Source6:    http://freedict.sourceforge.net/download/linux/%{dict6}.tar.gz
#Source7:    http://freedict.sourceforge.net/download/linux/%{dict7}.tar.gz
Source8:    http://freedict.sourceforge.net/download/linux/%{dict8}.tar.gz
Source9:    http://freedict.sourceforge.net/download/linux/%{dict9}.tar.gz
Source10:    http://freedict.sourceforge.net/download/linux/%{dict10}.tar.gz
Source11:    http://freedict.sourceforge.net/download/linux/%{dict11}.tar.gz
Source12:    http://freedict.sourceforge.net/download/linux/%{dict12}.tar.gz
Source13:    http://freedict.sourceforge.net/download/linux/%{dict13}.tar.gz
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


%prep
%setup -q -c
%setup -q -c -T -D -a 1
%setup -q -c -T -D -a 2
%setup -q -c -T -D -a 3
%setup -q -c -T -D -a 4
%setup -q -c -T -D -a 5
%setup -q -c -T -D -a 6
#%setup -q -c -T -D -a 7
%setup -q -c -T -D -a 8
%setup -q -c -T -D -a 9
%setup -q -c -T -D -a 10
%setup -q -c -T -D -a 11
%setup -q -c -T -D -a 12
%setup -q -c -T -D -a 13
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
%setup -q -c -T -D -a 25
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
for i in %{dictionaries}; do
    mv $i.dict.dz $i.gz
    gunzip $i.gz
    dictfiles=%{_datadir}/dictd/%{dictname}-$i
    ./dictmisc/dictfmt -f -u "%{URL}" -s "$i Freedict dictionary" %{dictname}_$i < $i
    dictzip %{dictname}_$i.dict
done


%install
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd,aqq}

for i in %{dictionaries}; do
    dictprefix=%{_datadir}/dictd/%{dictname}_$i
    echo "# The Bilingual dictionaries
    database $i {
        data  \"$dictprefix.dict.dz\"
        index \"$dictprefix.index\" 
    }
    " > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
    mv %{dictname}_%{dict1}*  $RPM_BUILD_ROOT%{_datadir}/dictd/
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

%files
%defattr(644,root,root,755)

%files -n  %{dictname}-%{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict1}*
