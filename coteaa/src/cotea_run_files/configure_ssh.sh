#!/bin/bash

echo "Creating directory"
mkdir -p /home/ubuntu/.ssh

echo "Adding keys"
mv ./id_rsa ./id_rsa.pub /home/ubuntu/.ssh/

echo "Changing .ssh dir owner"
chown -R root /home/ubuntu/.ssh/

echo "Changing .ssh dir mode to 700"
chmod 700 /home/ubuntu/.ssh/

# echo "Changing auth file mode"
# chmod 600  ~/.ssh/authorized_keysd
