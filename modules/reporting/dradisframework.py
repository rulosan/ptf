#!/usr/bin/env python
#######################################
# Installation module for Dradis Framework
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update - Dradis is a collaboration and reporting platform"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dradis/dradisframework.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dradisframework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="ruby1.9.1,ruby-rails-3.2,git,libsqlite-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},gem install bundler,ruby bin/setup,exit"

