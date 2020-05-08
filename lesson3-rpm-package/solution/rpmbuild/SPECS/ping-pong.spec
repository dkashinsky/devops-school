Name:           ping-pong
Version:        1.0
Release:        1%{?dist}
Summary:        Simple ping-pong web server application

License:        MIT
URL:            https://www.lineate.com/
Requires:       systemd
Requires:       java-headless
BuildArch:      noarch

%description
Simple ping-pong web server application

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/ping-pong
cp %{_sourcedir}/ping-pong.jar $RPM_BUILD_ROOT/usr/local/ping-pong/

mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
cp %{_sourcedir}/ping-pong.service $RPM_BUILD_ROOT/usr/lib/systemd/system/

%files
%defattr(-,root,root,-)
/usr/local/ping-pong/ping-pong.jar
/usr/lib/systemd/system/ping-pong.service

%post
systemctl daemon-reload
systemctl start ping-pong.service
systemctl enable ping-pong.service

%preun
systemctl stop ping-pong.service
systemctl disable ping-pong.service

%postun
rm -rf /usr/local/ping-pong

%changelog
* Sat Apr 25 2020 dkashinsky - initial package implementation
* Sat May 02 2020 dkashinsky - added uninstall scriptlets and required dependencies
- 
