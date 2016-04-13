# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('export_value', models.PositiveIntegerField()),
                ('import_value', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_id', models.PositiveIntegerField(max_length=255, choices=[(0, 'Afghanistan'), (1, 'Aland Islands'), (2, 'Albania'), (3, 'Algeria'), (4, 'American Samoa'), (5, 'Andorra'), (6, 'Angola'), (7, 'Anguilla'), (8, 'Antarctica'), (9, 'Antigua and Barbuda'), (10, 'Argentina'), (11, 'Armenia'), (12, 'Aruba'), (13, 'Australia'), (14, 'Austria'), (15, 'Azerbaijan'), (16, 'Bahamas'), (17, 'Bahrain'), (18, 'Bangladesh'), (19, 'Barbados'), (20, 'Belarus'), (21, 'Belgium'), (22, 'Belize'), (23, 'Benin'), (24, 'Bermuda'), (25, 'Bhutan'), (26, 'Bolivia (Plurinational State of)'), (27, 'Bonaire, Sint Eustatius and Saba'), (28, 'Bosnia and Herzegovina'), (29, 'Botswana'), (30, 'Bouvet Island'), (31, 'Brazil'), (32, 'British Indian Ocean Territory'), (33, 'Brunei Darussalam'), (34, 'Bulgaria'), (35, 'Burkina Faso'), (36, 'Burundi'), (37, 'Cabo Verde'), (38, 'Cambodia'), (39, 'Cameroon'), (40, 'Canada'), (41, 'Cayman Islands'), (42, 'Central African Republic'), (43, 'Chad'), (44, 'Chile'), (45, 'China'), (46, 'Christmas Island'), (47, 'Cocos (Keeling) Islands'), (48, 'Colombia'), (49, 'Comoros'), (50, 'Congo'), (51, 'Congo (Democratic Republic of the)'), (52, 'Cook Islands'), (53, 'Costa Rica'), (54, "Cote d'Ivoire"), (55, 'Croatia'), (56, 'Cuba'), (57, 'Curacao'), (58, 'Cyprus'), (59, 'Czech Republic'), (60, 'Denmark'), (61, 'Djibouti'), (62, 'Dominica'), (63, 'Dominican Republic'), (64, 'Ecuador'), (65, 'Egypt'), (66, 'El Salvador'), (67, 'Equatorial Guinea'), (68, 'Eritrea'), (69, 'Estonia'), (70, 'Ethiopia'), (71, 'Falkland Islands (Malvinas)'), (72, 'Faroe Islands'), (73, 'Fiji'), (74, 'Finland'), (75, 'France'), (76, 'French Guiana'), (77, 'French Polynesia'), (78, 'French Southern Territories'), (79, 'Gabon'), (80, 'Gambia'), (81, 'Georgia'), (82, 'Germany'), (83, 'Ghana'), (84, 'Gibraltar'), (85, 'Greece'), (86, 'Greenland'), (87, 'Grenada'), (88, 'Guadeloupe'), (89, 'Guam'), (90, 'Guatemala'), (91, 'Guernsey'), (92, 'Guinea'), (93, 'Guinea-Bissau'), (94, 'Guyana'), (95, 'Haiti'), (96, 'Heard Island and McDonald Islands'), (97, 'Holy See'), (98, 'Honduras'), (99, 'Hong Kong'), (100, 'Hungary'), (101, 'Iceland'), (102, 'India'), (103, 'Indonesia'), (104, 'Iran (Islamic Republic of)'), (105, 'Iraq'), (106, 'Ireland'), (107, 'Isle of Man'), (108, 'Israel'), (109, 'Italy'), (110, 'Jamaica'), (111, 'Japan'), (112, 'Jersey'), (113, 'Jordan'), (114, 'Kazakhstan'), (115, 'Kenya'), (116, 'Kiribati'), (117, "Korea (Democratic People's Republic of)"), (118, 'Korea (Republic of)'), (119, 'Kuwait'), (120, 'Kyrgyzstan'), (121, "Lao People's Democratic Republic"), (122, 'Latvia'), (123, 'Lebanon'), (124, 'Lesotho'), (125, 'Liberia'), (126, 'Libya'), (127, 'Liechtenstein'), (128, 'Lithuania'), (129, 'Luxembourg'), (130, 'Macao'), (131, 'Macedonia (the former Yugoslav Republic of)'), (132, 'Madagascar'), (133, 'Malawi'), (134, 'Malaysia'), (135, 'Maldives'), (136, 'Mali'), (137, 'Malta'), (138, 'Marshall Islands'), (139, 'Martinique'), (140, 'Mauritania'), (141, 'Mauritius'), (142, 'Mayotte'), (143, 'Mexico'), (144, 'Micronesia (Federated States of)'), (145, 'Moldova (Republic of)'), (146, 'Monaco'), (147, 'Mongolia'), (148, 'Montenegro'), (149, 'Montserrat'), (150, 'Morocco'), (151, 'Mozambique'), (152, 'Myanmar'), (153, 'Namibia'), (154, 'Nauru'), (155, 'Nepal'), (156, 'Netherlands'), (157, 'New Caledonia'), (158, 'New Zealand'), (159, 'Nicaragua'), (160, 'Niger'), (161, 'Nigeria'), (162, 'Niue'), (163, 'Norfolk Island'), (164, 'Northern Mariana Islands'), (165, 'Norway'), (166, 'Oman'), (167, 'Pakistan'), (168, 'Palau'), (169, 'Palestine, State of'), (170, 'Panama'), (171, 'Papua New Guinea'), (172, 'Paraguay'), (173, 'Peru'), (174, 'Philippines'), (175, 'Pitcairn'), (176, 'Poland'), (177, 'Portugal'), (178, 'Puerto Rico'), (179, 'Qatar'), (180, 'Reunion'), (181, 'Romania'), (182, 'Russian Federation'), (183, 'Rwanda'), (184, 'Saint Barthelemy'), (185, 'Saint Helena, Ascension and Tristan da Cunha'), (186, 'Saint Kitts and Nevis'), (187, 'Saint Lucia'), (188, 'Saint Martin (French part)'), (189, 'Saint Pierre and Miquelon'), (190, 'Saint Vincent and the Grenadines'), (191, 'Samoa'), (192, 'San Marino'), (193, 'Sao Tome and Principe'), (194, 'Saudi Arabia'), (195, 'Senegal'), (196, 'Serbia'), (197, 'Seychelles'), (198, 'Sierra Leone'), (199, 'Singapore'), (200, 'Sint Maarten (Dutch part)'), (201, 'Slovakia'), (202, 'Slovenia'), (203, 'Solomon Islands'), (204, 'Somalia'), (205, 'South Africa'), (206, 'South Georgia and the South Sandwich Islands'), (207, 'South Sudan'), (208, 'Spain'), (209, 'Sri Lanka'), (210, 'Sudan'), (211, 'Suriname'), (212, 'Svalbard and Jan Mayen'), (213, 'Swaziland'), (214, 'Sweden'), (215, 'Switzerland'), (216, 'Syrian Arab Republic'), (217, '[a]'), (218, 'Tajikistan'), (219, 'Tanzania, United Republic of'), (220, 'Thailand'), (221, 'Timor-Leste'), (222, 'Togo'), (223, 'Tokelau'), (224, 'Tonga'), (225, 'Trinidad and Tobago'), (226, 'Tunisia'), (227, 'Turkey'), (228, 'Turkmenistan'), (229, 'Turks and Caicos Islands'), (230, 'Tuvalu'), (231, 'Uganda'), (232, 'Ukraine'), (233, 'United Arab Emirates'), (234, 'United Kingdom of Great Britain and Northern Ireland'), (235, 'United States of America'), (236, 'United States Minor Outlying Islands'), (237, 'Uruguay'), (238, 'Uzbekistan'), (239, 'Vanuatu'), (240, 'Venezuela (Bolivarian Republic of)'), (241, 'Viet Nam'), (242, 'Virgin Islands (British)'), (243, 'Virgin Islands (U.S.)'), (244, 'Wallis and Futuna'), (245, 'Western Sahara'), (246, 'Yemen'), (247, 'Zambia'), (248, 'Zimbabwe')])),
                ('country_iso', models.CharField(help_text=b'This field fill automatically!', max_length=3)),
                ('country_name', models.CharField(help_text=b'This field fill automatically!', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.OneToOneField(null=True, blank=True, to='b2b_discount_module.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agreement',
            name='company',
            field=models.OneToOneField(null=True, blank=True, to='b2b_discount_module.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agreement',
            name='negotiator',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
