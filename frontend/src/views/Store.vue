<template>
  <v-card class="mx-auto my-12" max-width="600">
    <v-card-title> {{item.store_name}} </v-card-title>
    <v-card-text height="100%">
      <v-row align="center" class="mx-0">
        <v-rating
          :value="item.score"
          color="amber"
          dense
          half-increments
          readonly
          size="15"
        />
        <div class="grey--text ms-4">
          {{item.score}} ({{item.review_cnt}})
        </div>
      </v-row>
      <div class="text-body-2 mt-6">
        {{item.text1.slice().join(', ')}}
      </div>
      <div class="text-body-2 mt-6">
        {{item.text2.slice().join(', ')}}
      </div>
    </v-card-text>
    <v-spacer />
    <v-card-actions>
      <v-btn text color="teal accent-4" @click="$router.push('/')"> back </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Store",

  data: () => ({
    item: {}
  }),
  created() {
    this.item = this.$route.params;
    this.$vuetify.goTo(0)  
  },
  methods: {
    image_path(image) {
        return "static/image/" + image;
    }
  }
}
</script>
