<template>
    <v-card v-for="borrow in borrows" :key="borrow.id" class="mx-auto ma-4" :subtitle="borrow.user_name"
        :title="borrow.book_data.name">
        <v-card-text>{{ borrow.book_data.type }}</v-card-text>
        <v-card-actions>
            <v-btn append-icon="mdi-delete" color="red-lighten-2" variant="text" @click="returnBorrow(borrow.id)" />
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            borrows: []
        };
    },
    methods: {
        async fetchBorrows() {
            try {
                const response = await fetch('http://localhost:4000/borrows');
                if (!response.ok) throw new Error("Error fetching borrows");
                const data = await response.json();
                this.borrows = await Promise.all(
                    data.borrows.map(async (borrow) => {
                        const bookResponse = await fetch(
                            `http://localhost:4000/books/${borrow.book_id}`
                        );
                        const bookData = await bookResponse.json();
                        return { ...borrow, book_data: bookData.book };
                    })
                );
            } catch (error) {
                console.error("fetch borrows failed:", error);
                this.borrows = [];
            }
        },
        async returnBorrow(borrow_id) {
            try {
                const response = await fetch(
                    `http://localhost:4000/borrows/return/${borrow_id}`, {
                        method: "DELETE"
                    }
                );
                if (!response.ok) throw new Error("Failed to return borrow");
                await response.json();
                this.borrows = this.borrows.filter(borrow => borrow.id !== borrow_id);
            } catch (error) {
                console.error("Error:", error);
            }
        },
    },
    mounted() {
        this.fetchBorrows();
    }
};
</script>