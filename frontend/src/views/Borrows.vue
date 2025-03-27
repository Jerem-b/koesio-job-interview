<template>
    <v-container class="d-flex flex-column align-center justify-center">
        <h1>Borrows</h1>
        <div>
            <BorrowCreation/>
            <BorrowList/>
        </div>
    </v-container>
</template>

<script>
import BorrowCreation from '../components/BorrowCreation.vue';
import BorrowList from '../components/BorrowList.vue';

export default {
    components: {
        BorrowCreation,
        BorrowList,
    },
};
</script>