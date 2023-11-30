<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>305</width>
    <height>329</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: grey;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="title">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>201</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI</family>
      <pointsize>15</pointsize>
      <underline>true</underline>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;</string>
    </property>
    <property name="text">
     <string>Генератор паролів</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>231</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;</string>
    </property>
    <property name="text">
     <string>Тут буде результат </string>
    </property>
   </widget>
   <widget class="QCheckBox" name="cb_numbers">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;</string>
    </property>
    <property name="text">
     <string>Використовувати числа</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="cb_alphabet">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>241</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;</string>
    </property>
    <property name="text">
     <string>Використовувати алфавіт</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>200</y>
      <width>191</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true"> position: absolute;
    top:50%;
    background-color:#0a0a23;
    color: #fff;
    border:none;
    border-radius:10px;
    box-shadow: 0px 0px 2px 2px rgb(0,0,0);</string>
    </property>
    <property name="text">
     <string>Згенерувати</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
