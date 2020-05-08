Here are several steps and commands on the way to solve the issue:

1. Install rpm build tools
```sh
sudo dnf install rpm-build
```

2. Create `rpmbuild` folder with all the necessary folder structure. To do so run:
```sh
rpmdev-setuptree
```

3. Copy all the necessary application files into `rpmbuild/SOURCES` folder. For our case they are binary `.jar` and systemd `.service` files.

4. CD into `rpmbuild/SPECS` directory and create package spec file. To do so run:
```sh
cd rpmbuild/SPECS/
rpmdev-newspec app
```

5. Edit spec file according to your application needs. To build the package run:
```sh
cd ..
rpmbuild -bb ./SPECS/app.spec
```

6. To install the package run `sudo rpm -i package` where `package` points to the correct rpm. In my case:
```sh
sudo rpm -i ./RPMS/noarch/ping-pong-1.0-1.el8.noarch.rpm
```

7. To uninstall the package run `sudo rpm -e package` where `package` is the name of the package from `.spec` file:
```sh
rpm -e ping-pong
```
