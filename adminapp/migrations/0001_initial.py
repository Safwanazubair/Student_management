# Generated by Django 5.0.6 on 2024-11-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
                ('applied_on', models.CharField(max_length=100)),
                ('applied_by', models.CharField(max_length=100)),
                ('course_status', models.CharField(max_length=100)),
                ('payment_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='course_batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=100)),
                ('daily_hours', models.CharField(max_length=100)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='course_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryadd', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='course_certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateadd', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='course_duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durationadd', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='course_syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('syllabus_desc', models.CharField(max_length=100)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='course_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursetypeadd', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=1)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=100)),
                ('coursetype', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=100)),
                ('center', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('installment_no', models.CharField(max_length=100)),
                ('admission', models.CharField(max_length=100)),
                ('durationdigit', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('course_desc', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('is_popular', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='installments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=100)),
                ('order', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('maritalstatus', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('gcontact', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('isdelete', models.IntegerField(default=0)),
                ('is_complete', models.IntegerField(default=0)),
                ('added_by', models.IntegerField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
