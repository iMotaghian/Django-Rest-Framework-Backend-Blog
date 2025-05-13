from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    ## [ReadOnlyField] in serializer :
    # content = serializers.ReadOnlyField()
    # or
    # content = serializers.CharField(read_only=True)

    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = (
        serializers.SerializerMethodField()
    )  # function name is : get_absolute_url or -> SerializerMethodField(method_name='get_abs_url') -> def get_abs_url(self, obj):

    # category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all()) # 6-15 : default of category is id, this action return name of category from model(DB)
    # category = CategorySerializer() # ---> return: "category": {"id": 1,"name": "dev"},

    class Meta:
        model = Post
        # fields = "__all__"
        fields = [
            "id",
            "author",
            "title",
            "image",
            "category",
            "content",
            "snippet",
            "status",
            "relative_url",
            "absolute_url",
            "created_date",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):  # automatic is added to json export [get]
        rep = super().to_representation(instance)

        request = self.context.get("request")
        rep["state"] = "list"
        if request.parser_context.get("kwargs").get(
            "pk"
        ):  # check mikone bebine age pk vojod dashte bashe yani be "post-datails" rafte user va ye item ro mikhad
            rep["state"] = "single"
        if rep["state"] == "single":
            rep.pop("snippet", None)  # pop -> remove snippet or none
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)

        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data  # --->  "category": {"id": 1,"name": "dev"},
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )  # if we havent profile -> validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)
