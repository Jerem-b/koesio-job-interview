<template>
    <v-container class="d-flex flex-column align-center justify-center">
        <h1>Authors</h1>
        <div>
            <AuthorCreation/>
            <AuthorList/>
        </div>
    </v-container>
</template>

<script>
import AuthorCreation from '../components/AuthorCreation.vue';
import AuthorList from '../components/AuthorList.vue';

export default {
    components: {
        AuthorCreation,
        AuthorList,
    },
};
</script>