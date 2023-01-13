# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

# Copyright (C) 2023 Saatvik Nagpal

# This program is free software: under the terms of the GNU General 
# Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import mysql.connector as sqlcon
mydb=sqlcon.connect(host="localhost", user="root", password="student")


if mydb.is_connected():
          print("success")

mycursor=mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE reportcards")
    print("Database Created")
except:
    print("***Database exists..Creation of Database not required***")

mycursor.execute("USE reportcards")

try:
    mycursor.execute("""
    create table report(
    rollno varchar(20) NOT NULL,
    name varchar(20) NOT NULL,
    phym varchar(50) NOT NULL,
    chemm varchar(20) NOT NULL,
    mathm varchar(20) NOT NULL,
    engm varchar(20) NOT NULL,
    csm varchar(20) NOT NULL)""")

    print("TABLE CREATED")
except:
    print("***Table exists..Table Creation Not Required***")
