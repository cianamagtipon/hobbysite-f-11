# Generated by Django 4.2.10 on 2024-05-06 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_thread_alter_threadcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-created_on'], 'verbose_name': 'Thread', 'verbose_name_plural': 'Threads'},
        ),
        migrations.AlterModelOptions(
            name='threadcategory',
            options={'ordering': ['name'], 'verbose_name': 'Thread Category', 'verbose_name_plural': 'Thread Categories'},
        ),
        migrations.AlterField(
            model_name='thread',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='threads', to='forum.threadcategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.thread')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['created_on'],
            },
        ),
    ]
