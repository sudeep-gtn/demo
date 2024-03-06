from django.db import models
from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length = 255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product = models.OneToOneField(Product,on_delete = models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

# tag = Tag.objects.create(label = "Daily-use")
# tagged_item = TaggedItem.objects.create(content_object = tag)

# product = Product.objects.create(title = "Product1", description = 'This is product one ', price = 24, inventory = 'nothing', last_update = models.DateField.auto_now)


