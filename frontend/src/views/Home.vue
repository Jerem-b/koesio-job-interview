<template>
    <v-container class="d-flex flex-column align-center justify-center">
        <h1>BookFlow</h1>
        <img alt="Vue logo" class="logo" src="../assets/logo.svg" width="125" height="125" />
        <div>
            <SearchBook/>
        </div>
    </v-container>
</template>

<script>
import SearchBook from '../components/SearchBook.vue';

export default {
    components: {
        SearchBook
    },
};
</script>