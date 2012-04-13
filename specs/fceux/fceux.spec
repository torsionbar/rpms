Name: fceux
Version: 2.1.5
Release: 1

Summary: FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom Disk System (FDS) emulator

License: GPLv2
Group: Emulators
Url: http://fceux.com/web/home.html

Packager: George Nimmer <george164@earthlink.net>
Source0: http://downloads.sourceforge.net/fceultra/Source%20Code/%version%20src/%name-%version.src.tar.bz2


# Fixed desktop file and icons from previous version
Source1: fceux.desktop
Source2: fceux.png

BuildRequires: gcc-c++ gtk2-devel SDL-devel scons zlib-devel

%description
FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom Disk System
FDS) emulator. It supports both PAL (European) and NTSC (USA/JPN) modes. 
It supports both Windows and SDL versions for cross compatibility.
The FCEUX concept is that of an "all in one" emulator that offers accurate 
emulation and the best options for both casual play and a variety of more 
advanced emulator functions. For pro users, FCEUX offers tools for debugging, 
rom-hacking, map making, Tool-assisted movies, and Lua scripting

FCEUX is an evolution of the original FCE Ultra emulator. Over time FCE Ultra
had separated into many distinct branches. The concept behind FCEUX is to merge 
elements from FCEU Ultra, FCEU rerecording, FCEUXD, FCEUXDSP, FCEUXDSP CE, 
and FCEU-mm into a single branch of FCEU.

%prep
%setup

%build
CFLAGS="%optflags" scons

%install
# install binaries
install -D -m 755 bin/%name %buildroot/%_bindir/%name
install -D -m 755 bin/%name.chm %buildroot/%_bindir/%name.chm

# fix rights for docs
find documentation/ -type f -exec chmod -x {} \;
for i in Authors.txt changelog.txt NewPPUtests.txt README-SDL TODO-PROJECT TODO-SDL ; do
    chmod -x $i 
done

# install desktop and icons files
install -D -m 644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -D -m 644 %SOURCE2 %buildroot/%_iconsdir/%name.png

%files
%_bindir/*
%doc Authors.txt changelog.txt NewPPUtests.txt README-SDL TODO-PROJECT TODO-SDL documentation/*
%_iconsdir/*
%_desktopdir/*

%changelog
* Fri Apr 13 2012 George Nimmer <george164@earthlink.net> 2.1.5-1
- create spec file and initial build.
- add desktop and icons
