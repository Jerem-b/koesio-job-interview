<template>
    <v-container class="d-flex flex-column align-center justify-center">
        <h1>Books</h1>
        <div>
            <BookCreation />
            <BookList />
        </div>
    </v-container>
</template>

<script>
import BookCreation from '../components/BookCreation.vue';
import BookList from '../components/BookList.vue';

export default {
    components: {
        BookCreation,
        BookList,
    },
};
</script>