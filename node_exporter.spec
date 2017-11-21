Name: node_exporter
Version: 0.15.1
Release: 1
Summary: prometheus node_exporter
License: Apache-2.0
URL: https://github.com/lattebank/node_exporter

Source0: https://github.com/prometheus/node_exporter/releases/download/v%{version}/node_exporter-%{version}.linux-amd64.tar.gz
Source1: https://raw.githubusercontent.com/prometheus/node_exporter/v%{version}/examples/systemd/node_exporter.service
Source2: https://raw.githubusercontent.com/prometheus/node_exporter/v%{version}/examples/systemd/sysconfig.node_exporter

%description
prometheus node_exporter

%prep
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
tar xvzf node_exporter-%{version}.linux-amd64.tar.gz
mv sysconfig.node_exporter node_exporter

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}/%{_sbindir}
install -m 755 -d %{buildroot}/usr/lib/systemd/system
install -m 755 -d %{buildroot}/etc/sysconfig
install -m 755 node_exporter-%{version}.linux-amd64/node_exporter %{buildroot}/%{_sbindir}
install -m 644 node_exporter.service %{buildroot}/usr/lib/systemd/system/
install -m 644 node_exporter %{buildroot}/etc/sysconfig/

%files
/usr/sbin/node_exporter
/usr/lib/systemd/system/node_exporter.service
/etc/sysconfig/node_exporter

%pre
/usr/sbin/useradd node_exporter -s /sbin/nologin

%postun
/usr/sbin/userdel node_exporter

%changelog
